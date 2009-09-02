# -*- coding: utf-8 -*-
 
import pygame
import math
import random

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
    blowerGunFix2End = 52
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
        if self.shoot == True:
            airballCenter = ( self.location.centerx + self.blowerManLeft2Fix + ((self.blowerGunFix2End+10)*math.cos(self.angle)) ,\
                                self.location.bottom - self.blowerManButtom2Fix - ((self.blowerGunFix2End+10)*math.sin(self.angle)) )
            newAirball = Airball (self.game, airballCenter, self.angle)
            self.game.airballs.append (newAirball)
            self.shoot = False

        # draw the blower
        self.image.fill ((0,0,0,0))
        if ( self.angle > math.pi/2 ):
            blowerImg = self.game.res.blowerManLeft
        else:
            blowerImg = self.game.res.blowerMan
        self.image.blit (blowerImg, ( (Blower.imageWidth-self.game.res.blowerMan.get_width ())/2, (Blower.imageHeight-self.game.res.blowerMan.get_height()) ))
        rotatedGun = pygame.transform.rotozoom (self.game.res.blowerGun, math.degrees(self.angle), 1)
        rotatedRect = rotatedGun.get_rect()
        rotatedRect.center = (self.image.get_width()/2 + self.blowerManLeft2Fix, self.image.get_height()-self.blowerManButtom2Fix)
        self.image.blit (rotatedGun, rotatedRect)
        
class Airball (GraphicsBase):
    def __init__ (self, game, centerLoc, angle):
        GraphicsBase.__init__ (self,game)
        self.angle = angle
        self.image = pygame.transform.rotozoom (self.game.res.airball, math.degrees(self.angle), 1)
        self.location = pygame.Rect (0, 0, self.image.get_width (), self.image.get_height ())
        self.location.center = centerLoc
        self.posX, self.posY = centerLoc
        self.dead = False
        self.velocity = self.game.res.cfg.airballVelocity
    def think (self, time):
        self.velocity -= self.velocity * self.game.res.cfg.airballDrag * time
        self.posX += math.cos(self.angle)*self.velocity
        self.posY -= math.sin(self.angle) * self.velocity
        self.location.center = (self.posX, self.posY)

        if self.velocity < self.game.res.cfg.airballDieSpeed:
            self.dead = True
            return
        #collide with feather
        if self.game.feather.location.collidepoint(self.posX,self.posY):
            self.game.feather.hitbyairball(self)
            self.dead = True
        #collide with walls
        if self.posX - self.location.width/2 < 0:
            self.posX = self.location.width/2
            self.velocity *= self.game.res.cfg.airballBounce
            self.angle = math.pi - self.angle
        elif self.posX + self.location.width/2 > self.game.res.cfg.screenWidth:
            self.posX = self.game.res.cfg.screenWidth - self.location.width/2
            self.velocity *= self.game.res.cfg.airballBounce
            self.angle = math.pi - self.angle

class Feather (GraphicsBase):
    def __init__ (self,game):
        GraphicsBase.__init__ (self,game)
        self.dead = False
        self.game = game
        self.image = self.game.res.feather
        self.location = self.image.get_rect()
        self.location.center = (self.game.res.cfg.screenWidth/2, self.game.res.cfg.screenHeight/2)
        self.velX = 0.0
        self.velY = 0.0
        self.posX, self.posY = self.location.center
    def think(self,time):
        accelX = -self.velX * math.fabs(self.velX) * self.game.res.cfg.featherDragX
        self.velX += accelX * time

        accelY = -self.velY * math.fabs(self.velY) * self.game.res.cfg.featherDragY + self.game.res.cfg.featherGForce
        self.velY += accelY * time
        
        self.posX += self.velX * time
        self.posY += self.velY * time

        #stay inside map
        if self.posX - self.location.width/2 < 0:
            self.posX = self.location.width/2
            self.velX *= -0.5
        elif self.posX + self.location.width/2 > self.game.res.cfg.screenWidth:
            self.posX = self.game.res.cfg.screenWidth - self.location.width/2
            self.velX *= -0.5

        #rotate feather
        self.image = pygame.transform.rotozoom(self.game.res.feather,- self.velX * self.game.res.cfg.featherTilt,1)
        self.location = self.image.get_rect()
        self.location.center = (self.posX, self.posY)
    def hitbyfireball(self, fireball):
        self.velY = fireball.velocity + self.game.res.cfg.featherFireballHit # * self.game.res.cfg.featherFireballForce
    def hitbyairball(self, airball):
        magnitudeY = airball.velocity * self.game.res.cfg.featherBlowForceY
        magnitudeX = airball.velocity * self.game.res.cfg.featherBlowForceX
        self.velY -= (self.location.width/2 - math.fabs(self.posX - airball.posX)) * magnitudeY
        self.velX += (self.posX - airball.posX) * magnitudeX 


class Fireball (GraphicsBase):
    def __init__ (self,game,posX,posY,vel):
        GraphicsBase.__init__ (self,game)
        self.dead = False
        self.game = game
        self.image = self.game.res.fireball
        self.location = pygame.Rect (self.game.res.cfg.screenWidth/2, self.game.res.cfg.screenHeight/2,0,0)
        self.location.center = (posX, posY)
        self.velocity = vel
        self.rotationspeed = (random.random() - 0.5) * 10
        self.angle = 0.0
    def think(self,time):
        self.location.move_ip(0,self.velocity*time)
        oldcenter = self.location.center
        self.angle += self.rotationspeed
        while self.angle > 360:
            self.angle -= 360
        while self.angle < 0:
            self.angle += 360
        self.image = pygame.transform.rotozoom(self.game.res.fireball,self.angle,1)
        self.location = self.image.get_rect()
        self.location.center = oldcenter

        #die if below screen:
        if self.location.top > self.game.res.cfg.screenHeight:
            self.dead = True
        #collide with feather
        if self.game.feather.location.collidepoint(self.location.center):
            self.game.feather.hitbyfireball(self)

class EndNest (GraphicsBase):
    def __init__(self, game):
        GraphicsBase.__init__ (self,game)
        self.image = self.game.res.nest
        self.location = self.image.get_rect()
        self.location.left = self.game.res.cfg.screenWidth
        self.location.top = self.game.res.cfg.screenHeight * 0.75
        self.posRight = self.location.right
    def think(self,time):
        if self.location.right > self.game.res.cfg.screenWidth:
            self.posRight -= self.game.res.cfg.nestSpeed * time
            self.location.right = self.posRight

class BottomFire (GraphicsBase):
    def __init__ (self,game):
        GraphicsBase.__init__ (self,game)
        self.location = pygame.Rect (self.game.res.cfg.screenWidth/2, self.game.res.cfg.screenHeight-20)

