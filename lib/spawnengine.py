#! /usr/bin/env python
import random
import pygame
from graphics import Fireball

class Spawnengine:
    def __init__(self, game):
        self.game = game
        self.spawnqueue = []
 
        starttime = pygame.time.get_ticks()
        balls = self.game.res.cfg.ballsBase + self.game.level * self.game.res.cfg.ballsMultiplier #fireballs to spawn
        roundlength = ( self.game.res.cfg.roundlengthBase +  \
                self.game.level*self.game.res.cfg.roundlengthMultiplier)*1000 #roundlength in ms

        # one ball can spawn within this timefram
        timeframe =  roundlength / balls 
        
        random.seed()
        framestart = starttime
        while balls > 0:
            frameend = framestart + timeframe
            balls -= 1
            self.spawnqueue.append(random.randint(int(framestart),int(frameend)))
            framestart += timeframe

    def think(self,time):
        now = pygame.time.get_ticks()
        if len(self.spawnqueue) > 0:
            if self.spawnqueue[0] < now:
                del self.spawnqueue[0]
                posX = random.randint(0,self.game.res.cfg.screenWidth)
                posY = -80
                velY = self.game.res.cfg.ballsVelBase + random.random() * self.game.res.cfg.ballsVelGain
                velY += self.game.level * self.game.res.cfg.ballsVelLevelBoost 
                self.game.enemies.append(Fireball(self.game,posX,posY,velY))

