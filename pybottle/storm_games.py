#!/bin/python
# -*- coding: utf-8 -*-
"""Standard initializations and functions shared by all games."""

import os
from os import listdir
from os.path import isfile, join
import pygame
import time

def initialize_gui(gameTitle):
    # start pygame
    pygame.init()
    # start the display (required by the event loop)
    pygame.display.set_mode((320, 200))
    pygame.display.set_caption(gameTitle)
    # Load sounds from the sound directory
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


