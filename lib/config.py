# -*- coding: utf-8 -*-

from pygame.locals import *

class Config:
    def __init__ (self):
        self.keyLeft = K_a
        self.keyRight = K_d
        self.screenWidth = 640
        self.screenHeight = 480
       
        self.blowerVelocity = 0.5

        #round length is (base + level * multiplier) in seconds
        self.roundlengthBase = 12.0 
        self.roundlengthMultiplier = 1.2

        #number of fireballs for a round
        self.ballsBase = 10
        self.ballsMultiplier = 2
        #ball velocity
        self.ballsVelBase = 0.3
        self.ballsVelGain = 0.1
        self.ballsVelLevelBoost = 0.05
    
