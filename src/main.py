#première étape installer pygame et pytmx(carte) et pyscroll(déplacement et zoom sur la carte)  via le terminale (si ce n'est pas dèja fait)--> pip install pygame

import pygame

from src.game import Game

if __name__ == '__main__':
    pygame.init() #permet d'initialiser les composants contenu dans le module pygame
    game = Game()
    game.run()

