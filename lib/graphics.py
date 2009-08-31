# -*- coding: utf-8 -*-
 
import pygame

class GraphicsBase:
    def __init__ (self, game):
        self.game = game
    def draw (self):
        self.game.res.screen.blit (self.image, self.location)

class Blower (GraphicsBase):
    STOP = 0
    LEFT = 1
    RIGHT = 2
    def __init__ (self,game):
        GraphicsBase.__init__ (game)
        self.location = pygame.Rect (0,0,0,0);
        self.location.center(self.game.res.cfg.screenWidth/2, self.game.res.cfg.schreenHeight-10)
    def think (self, time):
        if (self.direction == LEFT):
            self.location.move_ip ( -self.game.res.cfg.blowerVelocity * time, 0)
        elif (self.direction == RIGHT):
            self.location.move_ip ( self.game.res.cfg.blowerVelocity * time, 0)
        
        # If mouse is within window, calculate new angle
        (mousePosX, mousePosY) = pygame.mouse.get_pos ()
        if ( mousePosX > 0 and mousePosX < self.game.res.cfg.screenWidth and \
                mousePosY > 0 and mousePosY < self.game.res.cfg.screenHeight ):
            pass

class Air (GraphicsBase):
    def __init__ (self, game, location):
        GraphicsBase.__init__ (game)
        self.location = location

class Feather (GraphicsBase):
    def __init__ (self,game):
        GraphicsBase.__init__ (game)
        self.location = pygame.Rect (self.game.res.cfg.screenWidth/2, self.game.res.cfg.schreenHeight/2)

class Fireball (GraphicsBase):
    def __init__ (self,game):
        GraphicsBase.__init__ (game)
        self.location = pygame.Rect (self.game.res.cfg.screenWidth/2, self.game.res.cfg.schreenHeight/2)

class BottomFire (GraphicsBase):
    def __init__ (self,game):
        GraphicsBase.__init__ (game)
        self.location = pygame.Rect (self.game.res.cfg.screenWidth/2, self.game.res.cfg.schreenHeight-20)

