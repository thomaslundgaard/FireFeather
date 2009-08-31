# -*- coding: utf-8 -*-
 
import pygame

class GraphicsBase:
    def __init__ (self, game):
        self.game = game
    def draw (self):
        self.game.res.screen.blit (self.image, self.location)

class Blower (GraphicsBase):
    origImage = pygame.image.load (os.path.join ("gfx", "blower.png")
    def __init__ (self,game):
        GraphicsBase.__init__ (game)
        self.location = pygame.Rect (self.game.res.cfg.screenWidth/2, self.game.res.cfg.schreenHeight-10)

class Air (GraphicsBase):
    origImage = pygame.image.load (os.path.join ("gfx", "air.png")
    def __init__ (self,game, location):
        GraphicsBase.__init__ (game)
        self.location = location

class Feather (GraphicsBase):
    origImage = pygame.image.load (os.path.join ("gfx", "feather.png")
    def __init__ (self,game):
        GraphicsBase.__init__ (game)
        self.location = pygame.Rect (self.game.res.cfg.screenWidth/2, self.game.res.cfg.schreenHeight/2)

class Fireball (GraphicsBase):
    origImage = pygame.image.load (os.path.join ("gfx", "fireball.png")
    def __init__ (self,game):
        GraphicsBase.__init__ (game)
        self.location = pygame.Rect (self.game.res.cfg.screenWidth/2, self.game.res.cfg.schreenHeight/2)

class BottomFire (GraphicsBase):
    origImage = pygame.image.load (os.path.join ("gfx", "bottomFire.png")
    def __init__ (self,game):
        GraphicsBase.__init__ (game)
        self.location = pygame.Rect (self.game.res.cfg.screenWidth/2, self.game.res.cfg.schreenHeight-20)

