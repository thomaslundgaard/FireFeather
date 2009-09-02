#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys
from graphics import Blower, Feather, TextObject, EndNest
from spawnengine import Spawnengine
from pygame.locals import *

class Game:
    STATE_PLAY = 0       # keep playing
    STATE_RESTART = 1    # restarts level (or next level if self.level has been incremented)
    STATE_GAME_OVER = 2  # return to menu
    STATE_LOSE_LIFE = 3  # lose a life and then restart level
    def __init__(self, level, resources):
        self.res = resources
        self.level = level
        self.life = 3
        self.state = self.STATE_RESTART
        self.enemies = []
        self.airballs = []
        self.effects = []
        self.feather = Feather(self)
        self.blower = Blower(self) 
        self.spawner = Spawnengine(self)
        self.clock = pygame.time.Clock()

    def run(self):
        while self.state == self.STATE_RESTART:
            self.state = self.STATE_PLAY
            self.enemies = []
            self.airballs = []
            self.effects = []
            self.feather = Feather(self)
            self.blower = Blower(self) 
            self.spawner = Spawnengine(self)
            TextObject (self, "Lives: "+str(self.life), -1, (10, 10))
            self.gameLoop ()

    def gameLoop (self):
        while True:
            # check state
            if self.state == self.STATE_PLAY:
                pass    # Continue with gameLoop
            elif self.state == self.STATE_LOSE_LIFE:
                self.life -= 1
                if self.life <= 0:
                    self.state = self.STATE_GAME_OVER
                else:
                    self.state = self.STATE_RESTART
                break
            else:
                break
            
            frametime = float(self.clock.tick(90)) #maxfps
            
            # Clear screen
            self.res.screen.blit(self.res.background, (0,0))

            #Get input
            self.handleInput()

            ## Update game objects
            self.spawner.think(frametime)
            self.blower.think(frametime)
            self.feather.think(frametime)
            for enemy in self.enemies:
                enemy.think(frametime)
            # Delete dead enemies
            self.enemies = [enemy for enemy in self.enemies if not enemy.dead]

            for airball in self.airballs:
                airball.think(frametime)
            # Delete dead airballs
            self.airballs = [airball for airball in self.airballs if not airball.dead]
            
            for effect in self.effects:
                effect.think(frametime)
            
            ## Draw game objects
            self.feather.draw()
            for enemy in self.enemies:
                enemy.draw()
            self.blower.draw()
            for airball in self.airballs:
                airball.draw()
            for effect in self.effects:
                effect.draw()

            pygame.display.flip()
            
    def handleInput(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.state = self.STATE_GAME_OVER
                    return
                else:
                    if self.res.cfg.keyLeft == event.key:
                        self.blower.direction = Blower.LEFT #TODO: Fix
                    elif self.res.cfg.keyRight == event.key:
                        self.blower.direction = Blower.RIGHT  #TODO: Fix
            elif event.type == KEYUP:
                if self.res.cfg.keyLeft == event.key:
                    if self.blower.direction == Blower.LEFT:
                        self.blower.direction = Blower.STOP
                if self.res.cfg.keyRight == event.key:
                    if self.blower.direction == Blower.RIGHT:
                        self.blower.direction = Blower.STOP
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.blower.shoot = True

    def loseLife (self):
        self.state = self.STATE_LOSE_LIFE
        
    def addEffect (self, effect):
        self.effects.append (effect)
        
    def removeEffect (self,  effect):
        self.effects.remove (effect)
