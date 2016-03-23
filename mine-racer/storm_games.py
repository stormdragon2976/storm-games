#!/bin/python
# -*- coding: utf-8 -*-
"""Standard initializations and functions shared by all games."""

import os
from os import listdir
from os.path import isfile, join
import pygame
import speechd
import time

spd = speechd.Client()
def speak(text, interupt = True):
    if interupt == True: spd.cancel()
    spd.say(text)

def exit_game():
    spd.close()
    pygame.quit()
    exit()

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
    soundData['game-intro'].play()
    time.sleep(soundData['game-intro'].get_length())
    return soundData

def game_menu(*options):
    loop = True
    pygame.mixer.music.load("sounds/music_menu.ogg")
    pygame.mixer.music.play(-1)
    i = 0
    speak(options[i])
    while loop == True:
        event = pygame.event.wait()
        if event.key == pygame.K_ESCAPE: exit_game()
        if event.key == pygame.K_DOWN and i < len(options) - 1:
            i = i + 1
            speak(options[i])
        if event.key == pygame.K_UP and i > 0:
            i = i - 1
            speak(options[i])
        event = pygame.event.clear()
        time.sleep(0.001)
