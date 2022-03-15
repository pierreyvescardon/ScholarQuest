from dataclasses import dataclass

import pygame, pytmx, pyscroll


from src import ListeQuestions


from src.ListeQuestions import questionnaire
from src.player import NPC
from src.anim import Anim_seq
from src.reponse_dialog import Reponse_DialogBox


@dataclass
class Portal:
    from_world: str#monde de depart
    origin_point: str#point de depart depuis ce monde
    target_world: str
    teleport_point: str



@dataclass  # décorateur : la classe en dessous vas absorber les caractéristiques de cette classe
class Map:  # pas de def __init__ car c'est une dataclasse
    name: str
    walls: list[pygame.Rect]  # la liste va contenir des rectangles de collision issu de la classe Rect de pygame
    group: pyscroll.PyscrollGroup
    tmx_data: pytmx.TiledMap # permet de recuperer l'ensemble des objets comme les spawns depuis nos fichier tmx
    portals: list[Portal] # permet d'avoir la liste des portail present sur la Map
    npcs: list[NPC]

class MapManager:

    def __init__(self, screen, player):
        self.maps = dict()  # ex "house" -> ("house", walls, group)
        self.screen = screen
        self.player = player
        self.current_map = "world"  # nom de la carte lancee par defaut
        self.anim_main = Anim_seq(path="C:/Users/Proprio/Desktop/ScholarQuest/animation/")

        self.registerMap("world", portals=[
            Portal(from_world="world", origin_point="enter_house", target_world="house", teleport_point="spawn_enter_house"),
            Portal(from_world="world", origin_point="enter_house2", target_world="house2", teleport_point="spawn_house"),
            Portal(from_world="world", origin_point="enter_dungeon", target_world="dungeon", teleport_point="spawn_dungeon")
        ], npcs=[NPC("paul", nb_points=7, dialog=ListeQuestions.questionnaire("Questions").questions, reponse=ListeQuestions.questionnaire("Questions").reponse,type="foe"),NPC("linux", nb_points=4, dialog=ListeQuestions.questionnaire("Questions").questions, reponse=ListeQuestions.questionnaire("Questions").reponse, type="prof")])
        self.registerMap("house", portals=[
            Portal(from_world="house", origin_point="exit_house", target_world="world", teleport_point="spawn_exit_house")
        ])
        self.registerMap("house2", portals=[
            Portal(from_world="house2", origin_point="exit_house", target_world="world",
                   teleport_point="exit_house2")
        ])
        self.registerMap("dungeon", portals=[
            Portal(from_world="dungeon", origin_point="exit_dungeon", target_world="world",
                   teleport_point="spawn_exit_dungeon")
        ])

        self.teleport_player("player")
        self.teleport_npcs()

    def check_npc_collision(self, dialog_box, reponse_box):
        for sprite in self.get_group().sprites():
            if sprite.feet.colliderect(self.player.rect) and type(sprite) is NPC and sprite.type=="prof":
                dialog_box.execute(sprite.dialog, sprite.reponse)

                if sprite.type == "prof": # ajoute la condition pour l ouverture de la boite dialogue de reponse
                    reponse_box.execute()


    def check_foe_collision(self):
        for sprite in self.get_group().sprites():
            if sprite.feet.colliderect(self.player.rect) and type(sprite) is NPC and sprite.type == "foe":
                return True

    def battle_instance(self):
        for sprite in self.get_group().sprites():
            if sprite.feet.colliderect(self.player.rect) and type(sprite) is NPC and sprite.type == "foe":
                self.registerBattleScreen(name=sprite.name)
                sprite.speed=0
                self.player.speed=0


    def collect_answer(self):
        for sprite in self.get_group().sprites():
            if sprite.feet.colliderect(self.player.rect) and type(sprite) is NPC:
                return sprite.reponse

    def check_collision(self):
        #gestion des portails
        for portal in self.get_map().portals:
            if portal.from_world == self.current_map:
                point = self.get_object(portal.origin_point)
                rect = pygame.Rect(point.x, point.y, point.width, point.height)

                if self.player.feet.colliderect(rect):
                    copy_portal = portal
                    self.current_map = portal.target_world
                    self.teleport_player(copy_portal.teleport_point)

        #gestion des collisions
        for sprite in self.get_group().sprites():

            if type(sprite) is NPC:
                if sprite.feet.colliderect(self.player.rect):
                    sprite.speed = 0
                else :
                    sprite.speed = 2

            if sprite.feet.collidelist(self.get_walls()) > -1:
                sprite.move_back()

    def teleport_player(self, name):
        point =self.get_object(name)
        self.player.position[0] = point.x #remplace la poisition initiale du player par la position en x
        self.player.position[1] = point.y
        self.player.save_location()#permet d'eviter les problematiques de collision apres teleportation avec des elements de type collision

    def registerMap(self, name, portals=[], npcs=[]):  # nom de la carte qui va etre chargee
        # charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame(f"C:/Users/Proprio/Desktop/ScholarQuest/map/{name}.tmx")
        map_data = pyscroll.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data,
                                                           self.screen.get_size())  # permet de charger les differents calques de notre fichier tmx. self.screen.get_size() indique la surface sur laquelle on veut afficher nos layer pour le coup map_data
        map_layer.zoom = 2  # fait un zoom en deux fois plus grand de ma carte

        # definir une liste qui va stocker les objets de types collision
        walls = []

        for obj in tmx_data.objects:  # recupere tous les objets de la carte
            if obj.type == "collision":
                walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de calques
        group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=6)  # default_layer est la position du calque par defaut ce qui peut etre utile si on veut mettre le joueur a un endroit de notre carte pour commencer
        group.add(self.player)  # j ajoute mon player au groupe de calque

        #recuperer tous les npcs pour les ajouter au groupe
        for npc in npcs:
            group.add(npc)

        # creer un objet Map
        self.maps[name] = Map(name, walls, group, tmx_data, portals, npcs)  # ajoute dans le dictionnaire les valeurs avec la clef name.

    def get_map(self):
        return self.maps[self.current_map]  # recuperer quel est l'objet de map actuel

    def get_group(self):
        return self.get_map().group  # renvoie le groupe de l'objet map recupere par get_map

    def get_walls(self):
        return self.get_map().walls

    def get_object(self, name): return self.get_map().tmx_data.get_object_by_name(name)#recupere certains objets de tmx_data grace a leur nom

    def teleport_npcs(self):
        for map in self.maps:
            map_data = self.maps[map]
            npcs = map_data.npcs

            for  npc in npcs:
                npc.load_points(map_data.tmx_data)
                npc.teleport_spawn()

    def draw(self):  # setter qui permet de recuperer la carte
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)  # place la camera sur le joueur directement

    def update(self):
        self.get_group().update()
        self.check_collision()

        for npc in self.get_map().npcs:
            npc.move()

    def registerBattleScreen(self,name):  # nom de l'ecran de combat qui va etre chargee
         #charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame(f"C:/Users/Proprio/Desktop/ScholarQuest/map/{name}.tmx")
        map_data = pyscroll.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data,
                                                           self.screen.get_size())  # permet de charger les differents calques de notre fichier tmx. self.screen.get_size() indique la surface sur laquelle on veut afficher nos layer pour le coup map_data
        map_layer.zoom = 1

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=8)
        self.group.draw(self.screen)
