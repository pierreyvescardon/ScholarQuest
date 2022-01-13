import pygame
import pytmx
import pyscroll

from player import Player
from src.dialog import DialogBox
from src.map import MapManager
from src.reponse_dialog import Reponse_DialogBox


class Game: #il faudra instancier la class game dans main pour pouvoir l utiliser

    def __init__(self): #fonction qui se fera au chargement de notre jeu

        # creer la fenetre du jeu
        self.screen = pygame.display.set_mode(((800, 600))) #le tuple indique la taille de fenetre en largeur et en hauter en pixel
        pygame.display.set_caption("ScholarQuest") #permet d indiquer le titre de la fenetre

        #Generer un joueur
        self.player = Player() # coordonnee initiale du joueur O,0
        self.map_manager = MapManager(self.screen, self.player)
        self.dialog_box = DialogBox()
        self.reponse_box = Reponse_DialogBox()
        self.input_txt = ""

    def handle_input(self): #methode pour prendre en charge les entrees claviers
        pressed = pygame.key.get_pressed() # variable qui recuperera absolument toute les touches entrees par le joueur

        if pressed[pygame.K_UP]:
            self.player.move_up()

        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation("down")
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation("left")
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation("right")


    def update(self): #actualisation du groupe
        self.map_manager.update()


    def run(self):

        clock = pygame.time.Clock() # va permettre de fixer les fps du jeu (frame per s)

        #boucle du jeu (permet de maintenir en activite cette fenetre sinon elle se referme instantanement)
        running = True # variable qui par defaut = True (donc fenetre ouverte)

        while running : #tant que la fenetre est active

            self.player.save_location()
            self.handle_input() #l'entreee clavier s'active avant tous les autres elements
            self.update() #permet d actualiser le groupe en permanence
            self.map_manager.draw()
            self.dialog_box.render(self.screen) #self.screen indique la surface sur laquelle applique la boite de dialogue
            self.reponse_box.render(self.screen)
            pygame.display.flip()# permet d'actualiser en temps reel et a chaque tout de boucle. Permet donc d'afficher l element precedent

            for event in pygame.event.get():
                if event.type == pygame.QUIT: #le joueur a clique sur la petite croix en haut de la fenetre
                    running = False #on quitte donc la boucle
                elif event.type == pygame.KEYDOWN: #correspond a nimporte quelle touche
                    if event.key == pygame.K_HASH: #button entrer
                        b=self.reponse_box.input_text
                        print(b)


                        self.map_manager.check_npc_collision(self.dialog_box, self.reponse_box)#passer à la prochaine phrase
                        a=self.dialog_box.question[self.dialog_box.text_index]
                        print(a)
                        if a==b:
                            print("youpi")
                        else:
                            print("pas encore ça")


                    elif event.key == pygame.K_BACKSPACE:
                        self.reponse_box.input_text = self.reponse_box.input_text[:-1]
                    else :
                        self.reponse_box.input_text += event.unicode




            clock.tick(60) # fps = 60

        pygame.quit()

#Utilisation de l outil tiled Map Editor pour la creation de la carte