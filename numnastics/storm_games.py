#!/bin/python
# -*- coding: utf-8 -*-
"""Standard initializations and functions shared by all games."""

import os
from os import listdir
from os.path import isfile, join
from inspect import isfunction
from xdg import BaseDirectory
import pygame
import random
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
    # Check for, and possibly create, storm-games path    
    global HOME
    HOME = BaseDirectory.xdg_config_home + "/storm-games"
    if not os.path.exists(HOME): os.makedirs(HOME)
    # Seed the random generator to the clock
    random.seed()
    # Set game's name
    global gameName
    gameName = gameTitle
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

def display_message(info):
    info.append("Press escape or enter to continue.")
    info.reverse()
    info.append("Use the up and down arrow keys to navigate this message.")
    info.reverse()
    i = 0
    speak(str(info[0:len(info)]))
    while True:
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN: return
            if event.key == pygame.K_DOWN and i < len(info) - 1: i = i + 1
            if event.key == pygame.K_UP and i > 0: i = i - 1
            speak(info[i])
        event = pygame.event.clear()
        time.sleep(0.001)
 
def instructions():
    info = (
        "Welcome to " + gameName + ": brought to you by Storm Dragon. Use the up and down arrows to navigate these instructions.",\
        "The object of the game is to arrange the random string of numbers so they read one through nine in as few tries as possible.",\
        "You can use the up or left arrow to move back in the string, and the down or right arrow to move forward, or close to the end of the string of numbers.",\
        "When you are on the number you want, press the enter key and that number, plus all the numbers to the end of the string, will be reversed.",\
        "For example, if you have the string of numbers 1 2 3 4 5 6 9 8 7, pressing enter while on the number 9 will reverse 9 8 7, making the string 1 2 3 4 5 6 7 8 9 and you will win the game.",\
        "If you need to her the string of numbers from your current position, press the spacebar.",\
        "Have fun, and good luck!",\
        "Press escape or enter to return to the game menu.")
    i = 0
    speak(info[i])
    while True:
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN: return
            if event.key == pygame.K_DOWN and i < len(info) - 1: i = i + 1
            if event.key == pygame.K_UP and i > 0: i = i - 1
            speak(info[i])
        event = pygame.event.clear()
        time.sleep(0.001)
 
def credits():
    info = (
        gameName + ": brought to you by Storm Dragon",\
        "Billy Wolfe, designer and coder.",\
        "http://stormdragon.tk",\
        "Press escape or enter to return to the game menu.")
    i = 0
    speak(info[i])
    while True:
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN: return
            if event.key == pygame.K_DOWN and i < len(info) - 1: i = i + 1
            if event.key == pygame.K_UP and i > 0: i = i - 1
            speak(info[i])
        event = pygame.event.clear()
        time.sleep(0.001)

def game_menu(*options):
    loop = True
    pygame.mixer.music.load("sounds/music_menu.ogg")
    pygame.mixer.music.set_volume(0.75)
    pygame.mixer.music.play(-1)
    i = 0
    speak(options[i])
    while loop == True:
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: exit_game()
            if event.key == pygame.K_DOWN and i < len(options) - 1: i = i + 1
            if event.key == pygame.K_UP and i > 0: i = i - 1
            if event.key == pygame.K_RETURN:
                try:
                    eval(options[i] + "()")
                    continue
                except:
                    pygame.mixer.music.fadeout(500)
                    time.sleep(0.25)
                    return options[i]
                    continue
            speak(options[i])
        event = pygame.event.clear()
        time.sleep(0.001)
