# -*- coding: utf-8 -*-

import resources
import pygame
import os
import time

class Main:
    def __init__ (self):
        self.res = resources.Resources ()
        pygame.init()
            
        #if self.cfg.sound and pygame.mixer:
            #pygame.mixer.pre_init(22100, -16, 16, 2048)
            #pygame.mixer.music.load(os.path.join('media','theme.ogg'))
            #pygame.mixer.music.play(-1)
        #if not self.cfg.sound:
            #pygame.mixer.quit()

        pygame.mouse.set_visible(True)
        pygame.display.set_caption("FireFeather")
        self.res.screen = pygame.display.set_mode((self.res.cfg.screenWidth, \
            self.res.cfg.screenHeight),0)

    def splash (self):
        splashImage = pygame.image.load (os.path.join ("gfx", "splash.png"))
        self.res.screen.fill ( (255,255,255))
        self.res.screen.blit (splashImage, (0,0))
        pygame.display.flip ()

        self.res.load ()
        time.sleep (5)
        
    def menu (self):
        pass
    