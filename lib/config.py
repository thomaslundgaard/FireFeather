# -*- coding: utf-8 -*-

from pygame.locals import *

class Config:
    def __init__ (self):
        self.keyLeft = K_a
        self.keyRight = K_d
        self.screenWidth = 640
        self.screenHeight = 480
       
        self.blowerVelocity = 0.3
        self.airballVelocity = 6.0
        self.airballDrag = 0.001
        self.airballBounce = 0.5
        self.airballDieSpeed = 0.8

        #round length is (base + level * multiplier) in seconds
        self.roundlengthBase = 12.0 
        self.roundlengthMultiplier = 1.2

        #number of fireballs for a round
        self.ballsBase = 10
        self.ballsMultiplier = 2
        #ball velocity
        self.ballsVelBase = 0.1
        self.ballsVelGain = 0.02
        self.ballsVelLevelBoost = 0.02

        #feather parameters
        self.featherGForce = 0.00004
        self.featherBlowForceY = 0.0002
        self.featherBlowForceX = 0.0003
        self.featherFireballHit = 0.01
        #self.featherFireballForce = 3.0
        #self.featherMaxSpeedX = 0.3
        #self.featherMaxSpeedY = 0.1
        self.featherDragX = 0.008
        self.featherDragY = 0.008
        self.featherTilt = 500.0

        #nest parameters
        self.nestSpeed = 0.02

    
