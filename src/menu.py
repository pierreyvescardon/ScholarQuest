import pygame
import pathlib
import os

class Menu_Box:

    X_POSITION = 0
    Y_POSITION = 440

    def __init__(self,numero=1):

        self.box = pygame.image.load((f"C:/Users/Proprio/Desktop/ScholarQuest/menu/battle_menu_{numero}.png"))
        self.box = pygame.transform.scale(self.box, (800,150))
        self.reading = True
        self.numero=numero
        self.length = len(os.listdir("C:/Users/Proprio/Desktop/ScholarQuest/menu/"))




    def render(self, screen):
        if self.reading:
            self.box = pygame.image.load((f"C:/Users/Proprio/Desktop/ScholarQuest/menu/battle_menu_{self.numero}.png"))
            self.box = pygame.transform.scale(self.box, (800, 150))
            screen.blit(self.box, (self.X_POSITION,self.Y_POSITION))



    def next_menu (self):
        self.numero+=1
        if self.numero > self.length:
            self.numero=1


    def previous_menu (self):
        self.numero-=1
        if self.numero < 1:
            self.numero=self.length



