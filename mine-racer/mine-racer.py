#!/bin/python
# -*- coding: utf-8 -*-

from storm_games import *

# Initial variable settings
mode = "menu"
sounds = initialize_gui("Mine Racer")

def game():
    pygame.mixer.music.load("sounds/music_car.ogg")
    gameOver = False
    jump = False
    points = 0
    position = 0
    while not gameOver:
        if pygame.mixer.music.get_busy() == 0 and jump == False: pygame.mixer.music.play(-1)
        event = pygame.event.wait()
        time.sleep(10)
        exit_game()

# Game starts at main menu
mode = game_menu("start game", "credits", "exit_game")
while True:
    # wait for an event
    event = pygame.event.wait()
    # if the event is about a keyboard button that have been pressed...
    if event.type == pygame.KEYDOWN:
        # Escape is the back/exit key, close the game if not playing, or return to menu if playing.
        if event.key == pygame.K_ESCAPE:
            if mode != "menu": mode = "menu"
            if mode == "menu": exit_game()
        # Call the game menu, if needed.
        if mode == "menu": mode = game_menu("start game", "credits", "exit_game")
        if mode == "start game": game()
    time.sleep(.001)

