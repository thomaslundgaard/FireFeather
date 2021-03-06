# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import os
import time

import resources
from game import Game

class Main:
    def __init__ (self):
        self.res = resources.Resources ()
        pygame.init()
            
        if not self.res.cfg.sound:
            pygame.mixer.quit()

        pygame.mouse.set_visible(True)
        pygame.display.set_caption("FireFeather")
        if self.res.cfg.fullscreen:
            scrFlag = FULLSCREEN
        else:
            scrFlag = 0
        self.res.screen = pygame.display.set_mode((self.res.cfg.screenWidth, \
            self.res.cfg.screenHeight),scrFlag)

    def splash (self):
        splashImage = pygame.image.load (os.path.join ("gfx", "splash.png"))
        self.res.screen.fill ((255,255,255))
        self.res.screen.blit (splashImage, (0,0))
        pygame.display.flip ()
        self.res.load ()
        time.sleep(1)
        
    def menu (self):
        while True:
            self.res.screen.fill ( (255,255,255))
            self.res.screen.blit (self.res.menuBackground, (0,0))
            pygame.display.flip ()
            
            play  = False
            while not play:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        return
                    elif event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            return
                        elif event.key == K_RETURN:
                            play = True
                            break

            play = False                
            game = Game (1,self.res)
            game.run ()
