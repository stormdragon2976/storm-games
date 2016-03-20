"""Standard initializations and functions shared by all games."""

import os
import pygame
import time

def initialize_gui(gameTitle):
    # start pygame
    pygame.init()
    # start the display (required by the event loop)
    pygame.display.set_mode((320, 200))
    pygame.display.set_caption(gameTitle)
    # Load sounds from the sound directory
    soundFileNames = next(os.walk("sounds/"))[2]
    for i in soundFileNames:
        if i[-4:] == ".ogg": i[:-4] = pygame.mixer.Sound("sounds/" + i)

