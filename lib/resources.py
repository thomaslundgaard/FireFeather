# -*- coding: utf-8 -*-

import config
import pygame
import os

class Resources:
    def __init__ (self):
        self.cfg = config.Config ()
        
    def load (self):
        self.background = pygame.image.load(os.join.path('gfx','background.png'))
