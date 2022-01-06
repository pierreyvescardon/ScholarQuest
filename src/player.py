import pygame

#un sprite est un element non statique qui peut interagir contrairement au decor
from src.animation import AnimateSprite


class Entity(AnimateSprite): # la classe Player va donc hériter de la classe Sprite présente dans pygame.sprite

    def __init__(self, name, x, y):
        super().__init__(name)   # initialisation du sprite
        self.image = self.get_image(0,0)
        self.image.set_colorkey([0,0,0])# indique la couleur de transparence pour le sprite
        self.rect = self.image.get_rect() #on definit un rectangle correspondant a la position du sprite
        self.position =[x, y] # pour pouvoir definir une position a notre joueur

        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12) #on fixe un rectangle au pied du joueur pour definir les collisions par la suite
        self.old_position = self.position.copy()


    def save_location(self): self.old_position =  self.position.copy()



    def move_right(self):
        self.change_animation("right")
        self.position[0] +=self.speed # le 0 correspond à la position x (l'indice 0 de la liste self position)

    def move_left(self):
        self.change_animation("left")
        self.position[0] -=self.speed

    def move_up(self):
        self.change_animation("up")
        self.position[1] -=self.speed # le 1 correspond à la position y (l'indice 1 de la liste self position)

    def move_down(self):
        self.change_animation("down")
        self.position[1] +=self.speed



    def update(self) : # va etre automatiquement appelee en permanence dans le jeu pour mettre a jour la position du joueur
        self.rect.topleft = self.position
        self.feet.midbottom =  self.rect.midbottom

    def move_back(self): #permet que lorsque le joueur entre en collision de se replacer dans la position precedente
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom


class Player(Entity):

    def __init__(self):
        super().__init__("player",0,0)

class NPC(Entity):

    def __init__(self, name, nb_points, dialog, reponse):
        super().__init__(name,0,0)
        self.nb_points = nb_points
        self.dialog = dialog
        self.reponse = reponse
        self.points=[]
        self.name = name
        self.speed = 1
        self.current_point=0

    def move(self):
        current_point = self.current_point
        target_point = self.current_point + 1

        if target_point >= self.nb_points:
            target_point=0

        current_rect = self.points[current_point]
        target_rect = self.points[target_point]

        if current_rect.y < target_rect.y and abs (current_rect.x - target_rect.x) < 3 : # la premiere condition verifie que le position courante est au dessus de celle cible, la deuxieme
            self.move_down()
        elif  current_rect.y > target_rect.y and abs (current_rect.x - target_rect.x) < 3 : # la premiere condition verifie que le position courante est au dessus de celle cible, la deuxieme
            self.move_up()
        elif current_rect.x < target_rect.x and abs (current_rect.y - target_rect.y) < 3 : # la premiere condition verifie que le position courante est au dessus de celle cible, la deuxieme
            self.move_right()
        elif current_rect.x > target_rect.x and abs (current_rect.y - target_rect.y) < 3 : # la premiere condition verifie que le position courante est au dessus de celle cible, la deuxieme
            self.move_left()

        if self.rect.colliderect(target_rect):
            self.current_point = target_point


    def teleport_spawn(self):
        location = self.points[self.current_point]
        self.position[0] = location.x
        self.position[1] = location.y
        self.save_location()

    def load_points(self, tmx_data):
        for num in range(1, self.nb_points+1):
            point = tmx_data.get_object_by_name(f"{self.name}_path{num}")
            rect = pygame.Rect(point.x, point.y, point.width, point.height)
            self.points.append(rect)