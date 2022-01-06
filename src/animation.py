import pygame


class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, name):
        super().__init__() #si on appele pas cette super classe, l'heritage ne fonctionne pas
        self.sprite_sheet = pygame.image.load(f"C:/Users/Proprio/Desktop/ScholarQuest/sprite/{name}.png")
        self.animation_index = 0 # par default on veut afficher la premiere image de notre liste d'image
        self.clock = 0
        self.images = {
            # on va creer un dico qui contiendra nos differentes image du joueur en fonction des action indiquées
            "down": self.get_images(0),  # premiere ligne d'images
            "left": self.get_images(32),
            "right": self.get_images(64),
            "up": self.get_images(96)
        }
        self.speed = 2  # vitesse de déplacement

    def change_animation(self, name):
        self.image = self.images[name][self.animation_index] # methode qui va permettre de changer l'image en fonction de la clef indiqué name indiqué, on fera ce changement au moment d'un input
        self.image.set_colorkey(0,0) # necessaire pour que la nouvelle image chargé n'est pas le fond noir
        self.clock += self.speed * 8 #va indiquer la vitesse des changement d'animation

        if self.clock >=100:

            self.animation_index += 1 # passer au sprite suivant

            if self.animation_index >= len(self.images[name]):
                self.animation_index = 0

            self.clock = 0

    def get_image(self, x, y): #permet de recuper la partie de l image que l on souhaite avec ses coordonnees ex : 0,0 pour la premiere image
        image = pygame.Surface([32, 32]) #32,32 correspond a la surface couverte par le personnage
        image.blit(self.sprite_sheet,(0,0),(x,y,32,32))# on extrait un morceau de l image qui par defaut sera de coordonnees 0,0
        return image

    def get_images(self, y):
        images = []

        for i in range (0,3):
            x = i*32 #incremente de 32 a chaque boucle
            image = self.get_image(x, y)
            images.append(image)

        return images
