#!/bin/python
# -*- coding: utf-8 -*-

from storm_games import *

# Initial variable settings
mode = "menu"
sounds = initialize_gui("Numnastics")

def game(mode):
    i = 0
    tries = 0
    numberList = list("123456789")
    random.shuffle(numberList)
    while ''.join(numberList) != "123456789":
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            # Escape is the back/exit key, close the game if not playing, or return to menu if playing.
            if event.key == pygame.K_ESCAPE:
                if mode != "menu":
                    mode = "menu"
                    return mode
                elif mode == "menu": exit_game()
            elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6,pygame.K_7, pygame.K_8, pygame.K_9]:
                i = numberList.index((pygame.key.name(event.key)))
                speak(numberList[i])
            elif event.key in [pygame.K_LEFT, pygame.K_UP]:
                if i > 0: i = i - 1
                speak(numberList[i])
            elif event.key in [pygame.K_RIGHT, pygame.K_DOWN]:
                if i < len(numberList) - 1: i = i + 1
                speak(numberList[i])
            elif event.key == pygame.K_SPACE:
                speak(str(' '.join(numberList[i:len(numberList)])))
                continue
            elif event.key == pygame.K_RETURN:
                if i != -1:
                    reversedNumberList = numberList[i:len(numberList)]
                    reversedNumberList.reverse()
                    del numberList[i:len(numberList)]
                    numberList.extend(reversedNumberList)
                    tries = tries + 1
                    sounds['flip'].play()
                    speak(str(' '.join(numberList[i:len(numberList)])))
            else:
                i = -1
                sounds['error'].play()
    sounds['win'].play()
    speak("solved in " + str(tries) + " tries.")
    return "menu"

# Game starts at main menu
mode = game_menu("start game", "instructions", "credits", "exit_game")
while True:
    try:
        if event.type == pygame.KEYDOWN:
            # Escape is the back/exit key, close the game if not playing, or return to menu if playing.
            if event.key == pygame.K_ESCAPE:
                if mode != "menu": mode = "menu"
                if mode == "menu": exit_game()
            # Call the game menu, if needed.
            if mode == "menu": mode = game_menu("start game", "instructions", "credits", "exit_game")
            if mode == "start game": mode = game(mode)
    except:
        pass    
# wait for an event
    event = pygame.event.wait()
    time.sleep(.001)

