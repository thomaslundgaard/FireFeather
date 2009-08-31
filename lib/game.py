#! /usr/bin/env python

import pygame
import sys
from graphics import Blower
from spawnengine import Spawnengine
from pygame.locals import *

class Game:
    def __init__(self, level, resources):
        self.quit = False
        self.level = level
        self.res = resources
        self.enemies = []
        self.airballs = []
        self.effects = []
        self.feather = None #TODO
        self.blower = Blower(self) 
        self.clock = pygame.time.Clock()

        self.spawner = Spawnengine(self)
    def run(self):
        while not self.quit:
            frametime = float(self.clock.tick(90)) #maxfps
            
            # Clear screen
            self.res.screen.blit(self.res.background, (0,0))

            #Get input
            self.handleInput()

            ## Update game objects
            self.spawner.think(frametime)
            self.blower.think(frametime)
            #TODO: self.feather.think(frametime)
            for enemy in self.enemies:
                enemy.think(frametime)
            # Delete dead enemies
            self.enemies = [enemy for enemy in self.enemies if not enemy.dead]

            for effect in self.effects:
                effect.think(frametime)
            self.effects = [effect for effect in self.effects if not effect.dead]

            ## Draw game objects
            for enemy in self.enemies:
                enemy.draw()
            self.blower.draw()
            for air in self.airballs:
                air.draw()
            for effect in self.effects:
                effect.draw()

            pygame.display.flip()
    def handleInput(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.quit = True
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
