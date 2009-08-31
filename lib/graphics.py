# -*- coding: utf-8 -*-
 
import pygame
import math

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
    blowerManLeft2Fix = 3
    def __init__ (self,game):
        GraphicsBase.__init__ (self,game)
        self.location = pygame.Rect (0,0,Blower.imageWidth,Blower.imageHeight);
        self.location.midbottom = (self.game.res.cfg.screenWidth/2, self.game.res.cfg.screenHeight)
        self.angle = 0
        img = pygame.Surface ((Blower.imageWidth, Blower.imageHeight))
        self.image = img.convert_alpha()
        self.direction = Blower.STOP
        self.shoot = False
    def think (self, time):
        if (self.direction == Blower.LEFT):
            self.location.move_ip ( -self.game.res.cfg.blowerVelocity * time, 0)
        elif (self.direction == Blower.RIGHT):
            self.location.move_ip ( self.game.res.cfg.blowerVelocity * time, 0)
        
        if (self.location.left < 0):
            self.location.left = 0
        if (self.location.right > self.game.res.cfg.screenWidth):
            self.location.right = self.game.res.cfg.screenWidth

        # If mouse is within window, calculate new angle (else use old angle)
        (mouseX, mouseY) = pygame.mouse.get_pos ()
        if ( mouseX > 0 and mouseX < self.game.res.cfg.screenWidth and \
                mouseY > 0 and mouseY < self.game.res.cfg.screenHeight ):
            self.angle = math.atan2 ( self.game.res.cfg.screenHeight - self.blowerManButtom2Fix - mouseY, \
                mouseX - self.location.centerx + self.blowerManLeft2Fix)
    
        # if we are shooting, create new airball
        airballLocation = pygame.Rect (0,0,0,0)
        airballLocation.left = 2
        newAirball = Airball (self.game, airballLocation, self.angle)
        self.game.airballs.append (newAirball)

        # draw the blower
        self.image.fill ((0,0,0,0))
        self.image.blit (self.game.res.blowerMan, ( (Blower.imageWidth-self.game.res.blowerMan.get_width ())/2, (Blower.imageHeight-self.game.res.blowerMan.get_height()) ))
        rotatedGun = pygame.transform.rotozoom (self.game.res.blowerGun, math.degrees(self.angle), 1)
        rotatedRect = rotatedGun.get_rect()
        rotatedRect.center = (self.image.get_width()/2 + self.blowerManLeft2Fix, self.image.get_height()-self.blowerManButtom2Fix)
        self.image.blit (rotatedGun, rotatedRect)
        
class Airball (GraphicsBase):
    def __init__ (self, game, location, angle):
        GraphicsBase.__init__ (self,game)
        self.location = location
        self.angle = angle
        self.dead = False
        self.image = pygame.transform.rotozoom (self.game.res.airball, self.angle, 1)
    def think (self):
        pass

class Feather (GraphicsBase):
    def __init__ (self,game):
        GraphicsBase.__init__ (self,game)
        self.dead = False
        self.location = pygame.Rect (self.game.res.cfg.screenWidth/2, self.game.res.cfg.screenHeight/2)

class Fireball (GraphicsBase):
    def __init__ (self,game,posX,posY,vel):
        GraphicsBase.__init__ (self,game)
        self.dead = False
        self.image = pygame.Surface((10,10)) #TODO
        self.location = pygame.Rect (self.game.res.cfg.screenWidth/2, self.game.res.cfg.screenHeight/2,0,0)
    def think(self,time):
        pass #TODO

class BottomFire (GraphicsBase):
    def __init__ (self,game):
        GraphicsBase.__init__ (self,game)
        self.location = pygame.Rect (self.game.res.cfg.screenWidth/2, self.game.res.cfg.screenHeight-20)

