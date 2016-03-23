#!/bin/python
# -*- coding: utf-8 -*-

from storm_games import *

# Initial variable settings
mode = "menu"
gameName = "Mine Racer"
sounds = initialize_gui(gameName)

# Game starts at main menu
mode = game_menu("start game", "credits", "exit")
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
        if mode == "menu": mode = game_menu("start game", "credits", "exit")
    time.sleep(.001)
