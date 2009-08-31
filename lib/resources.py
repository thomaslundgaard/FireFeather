# -*- coding: utf-8 -*-

import pygame
import os

import config
import pygame
import os

class Resources:
    def __init__ (self):
        self.cfg = config.Config ()
        
    def load (self):
        self.menuBackground = pygame.image.load (os.path.join ("gfx", "menuBackground.png"))
        self.blowerMan = pygame.image.load (os.path.join ("gfx", "blowerMan.png"))
        self.blowerGun = pygame.image.load (os.path.join ("gfx", "blowerGun.png"))
        self.background = pygame.image.load(os.path.join ('gfx','background.png'))
