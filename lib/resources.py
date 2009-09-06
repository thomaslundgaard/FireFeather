# -*- coding: utf-8 -*-

import pygame
import os

import config
import pygame
import os
from animation import Animation

class Resources:
    def __init__ (self):
        self.cfg = config.Config ()
        
    def load (self):
        self.font = pygame.font.Font(os.path.join("fonts", "TerminusBold.ttf"),  28)
        self.menuBackground = pygame.image.load (os.path.join ("gfx", "menuBackground.png"))
        self.menuBackground = self.menuBackground.convert_alpha ()
        self.blowerMan = pygame.image.load (os.path.join ("gfx", "blowerMan.png"))
        self.blowerMan = self.blowerMan.convert_alpha ()
        self.blowerManBlink = pygame.image.load( os.path.join('gfx','blowerManBlink.png'))
        self.blowerManBlink = self.blowerManBlink.convert_alpha()
        self.blowerManLeft = pygame.transform.flip (self.blowerMan, 1, 0)
        self.blowerManBlinkLeft = pygame.transform.flip( self.blowerManBlink, 1, 0)
        self.blowerGun = pygame.image.load (os.path.join ("gfx", "blowerGun.png"))
        self.blowerGun = self.blowerGun.convert_alpha ()
        self.blowerManDie = Animation(os.path.join('gfx','die.png'),50,100)
        self.airball = pygame.image.load (os.path.join ("gfx", "airball.png"))
        self.airball = self.airball.convert_alpha ()
        self.background = pygame.image.load(os.path.join ('gfx','background.png'))
        self.background = self.background.convert ()
        self.feather = pygame.image.load(os.path.join('gfx','feather.png'))
        self.feather = self.feather.convert_alpha()
        self.fireball = pygame.image.load(os.path.join('gfx','fireball.png'))
        self.fireball = self.fireball.convert_alpha ()
        self.nest = pygame.image.load(os.path.join('gfx','nest.png'))
        self.nest = self.nest.convert_alpha ()
