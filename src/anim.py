import pygame
import time
import os


class Anim_seq:
    X_POSITION = 0
    Y_POSITION = 440

    def __init__(self, path):

        self.path = path
        self.animation_sprite = os.listdir(self.path)
        self.compteur=0
        self.box=pygame.image.load(f"{path}{self.animation_sprite[self.compteur]}")
        self.box = pygame.transform.scale(self.box, (800, 150))
        self.length = len(os.listdir(self.path))
        self.reading = True


    def update (self,screen):
        if self.reading:
            if self.compteur < (self.length-1):
                self.render(screen)
                self.compteur += 1
            else :
                self.render(screen)
                self.reading = False

    def update_loop (self,screen):
        if self.reading:
            if self.compteur < (self.length-1):
                self.render(screen)
                self.compteur += 1
            else :
                self.render(screen)
                self.compteur=0


    def render(self, screen):
        if self.reading:
            self.box = pygame.image.load(f"{self.path}{self.animation_sprite[self.compteur]}")
            self.box = pygame.transform.scale(self.box, (800, 150))
            screen.blit(self.box, (self.X_POSITION, self.Y_POSITION))

    def seq_image (self,screen):
        if self.reading:
            for i in range (self.length):
                self.compteur=i
                self.render(screen)
                pygame.time.wait(500)








