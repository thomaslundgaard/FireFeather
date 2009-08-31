#! /usr/bin/env python

import pygame

class Game:
    def __init__(self, level, resources):
        self.quit = false
        self.level = level
        self.res = resources
        self.enemies = []
        self.blower = None #TODO
        self.clock = pygame.time.Clock()
    def run(self):
        while not self.quit:
            pass
     

        
