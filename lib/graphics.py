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
    imageWidth = 110
    imageHeight = 85
    blowerManButtom2Fix = 16
    blowerGunLeft2Fix = 84
    def __init__ (self,game):
        GraphicsBase.__init__ (game)
        self.location = pygame.Rect (0,0,imageWidth,imageHeight);
        self.location.midbottom = (self.game.res.cfg.screenWidth/2, self.game.res.cfg.schreenHeight)
        self.angle = 0
        self.image = pygame.surface (imageWidth, imageHeight)
    def think (self, time):
        if (self.direction == LEFT):
            self.location.move_ip ( -self.game.res.cfg.blowerVelocity * time, 0)
        elif (self.direction == RIGHT):
            self.location.move_ip ( self.game.res.cfg.blowerVelocity * time, 0)
        
        if (self.location.left < 0):
            self.location.left = 0
        if (self.location.right > self.game.res.cfg.screenWidth):
            self.location.right = self.game.res.cfg.screenWidth

        # If mouse is within window, calculate new angle (else use old angle)
        (mouseX, mouseY) = pygame.mouse.get_pos ()
        if ( mouseX > 0 and mouseX < self.game.res.cfg.screenWidth and \
                mouseY > 0 and mouseY < self.game.res.cfg.screenHeight ):
            self.angle = atan2 ( self.game.res.cfg.screenHeight-blowerManButtom2Fix-mouseY, (-1)*(self.game.res.cfg.screenWidth-mouseX-imageWidth/2) )

        # draw the blower
        self.image.fill ((0,0,0,0))
        self.image.blit (self.res.blowerMan, ( (imageWidth-self.res.blowerMan.get_width ())/2, (imageHeight-self.res.blowerMan.get_height()) ))
        
        
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

