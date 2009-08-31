# -*- coding: utf-8 -*-

import pygame
import os

import config

class Resources:
    def __init__ (self):
        self.cfg = config.Config ()
        
    def load (self):
        self.blowerMan = pygame.image.load (os.path.join ("gfx", "blowerMan.png"))
        self.blowerGun = pygame.image.load (os.path.join ("gfx", "blowerGun.png"))
