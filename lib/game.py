#! /usr/bin/env python

import pygame

class Game:
    def __init__(self, level, resources):
        self.quit = False
        self.level = level
        self.res = resources
        self.enemies = []
        self.effects = []
        self.feather = None #TODO
        self.blower = None #TODO
        self.clock = pygame.time.Clock()
    def run(self):
        while not self.quit:
            frametime = float(self.clock.tick(90)) #maxfps
            
            self.res.screen.blit(self.res.background, (0,0)) #Clear screen

            #update game objects
            self.blower.think(frametime)
            self.feather.think(frametime)
            for enemy in self.enemies:
                enemy.think(frametime)
            #delete dead enemies
            self.enemies = [enemy for enemy in self.enemies if not enemy.dead]

            for effect in self.effects:
                effect.think(frametime)
            self.effects = [effect for effect in self.effects if not effect.dead]
            




            

