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
        self.menuBackground = self.menuBackground.convert_alpha ()
        self.blowerMan = pygame.image.load (os.path.join ("gfx", "blowerMan.png"))
        self.blowerMan = self.blowerMan.convert_alpha ()
        self.blowerGun = pygame.image.load (os.path.join ("gfx", "blowerGun.png"))
        self.blowerGun = self.blowerGun.convert_alpha ()
        self.airball = pygame.image.load (os.path.join ("gfx", "airball.png"))
        self.airball = self.airball.convert_alpha ()
        self.background = pygame.image.load(os.path.join ('gfx','background.png'))
        self.background = self.background.convert ()
        self.feather = pygame.image.load(os.path.join('gfx','feather.png'))
        self.feather = self.feather.convert_alpha()
        self.fireball = pygame.image.load(os.path.join('gfx','fireball.png'))
        self.fireball = self.fireball.convert_alpha ()
