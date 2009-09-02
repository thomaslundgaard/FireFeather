#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys
from graphics import Blower, Feather, EndNest
from spawnengine import Spawnengine
from pygame.locals import *

class Game:
    STATE_PLAY = 0       # keep playing
    STATE_RESTART = 1    # restarts level (or next level if self.level has been incremented)
    STATE_GAME_OVER = 2  # retrun to menu
    def __init__(self, level, resources):
        self.state = self.STATE_PLAY
        self.level = level
        self.res = resources
        self.enemies = []
        self.airballs = []
        self.effects = []
        self.feather = Feather(self)
        self.blower = Blower(self) 
        self.clock = pygame.time.Clock()
        self.spawner = Spawnengine(self)

    def run(self):
        while self.state == self.STATE_PLAY or self.state == self.STATE_RESTART:
            self.state = self.STATE_PLAY
            self.gameLoop ()
            self.enemies = []
            self.airballs = []
            self.effects = []
            self.feather = Feather(self)
            self.blower = Blower(self) 

    def gameLoop (self):
        while self.state == self.STATE_PLAY:
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

            for airball in self.airballs:
                airball.think(frametime)
            # Delete dead airballs
            self.airballs = [airball for airball in self.airballs if not airball.dead]
            
            for effect in self.effects:
                effect.think(frametime)
            self.effects = [effect for effect in self.effects if not effect.dead]

            ## Draw game objects
            self.feather.draw()
            for enemy in self.enemies:
                enemy.draw()
            self.blower.draw()
            for airball in self.airballs:
                airball.draw()
            for effect in self.effects:
                effect.draw()

            # Time for nest to appear?
            if not self.spawner.spawnqueue: #spawnqueue empty
                if not self.enemies:
                    EndNest(self)

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
