#!/bin/python
# -*- coding: utf-8 -*-
# Shoot the bottles as fast as possible.

from storm_games import *

sounds = initialize_gui("Bottle Blaster")

# loop forever (until a break occurs)
while True:
    # wait for an event
    event = pygame.event.wait()
    # if the event is about a keyboard button that have been pressed...
    if event.type == pygame.KEYDOWN:
        sounds['bottle'].play(-1)
    if event.type == pygame.KEYUP:
        sounds['bottle'].stop()
        # and if the button is the "q" letter or the "escape" key...
        if event.key == pygame.K_ESCAPE:
            # ... then exit from the while loop
            break
    time.sleep(.001)
