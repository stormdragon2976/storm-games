#!/bin/python
# -*- coding: utf-8 -*-
"""Standard initializations and functions shared by all games."""

import os
from os import listdir
from os.path import isfile, join
import pygame
import time

SoundFolder = 'sounds'

def initialize_gui(gameTitle):
    # start pygame
    pygame.init()
    # start the display (required by the event loop)
    pygame.display.set_mode((320, 200))
    pygame.display.set_caption(gameTitle)
    # Load sounds from the sound directory and creates a list like that {'bottle': 'bottle.ogg'}
    soundFiles = [f for f in listdir("sounds/") if isfile(join("sounds/", f)) and (f.split('.')[1].lower() in ["ogg","wav"])]
    #lets make a dict with pygame.mixer.Sound() objects {'bottle':<soundobject>}
    soundData = {}
    for f in soundFiles:
        soundData[f.split('.')[0]] = pygame.mixer.Sound("sounds/" + f)
    return soundData
