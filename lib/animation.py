import pygame
from pygame.locals import *
class Animation:
    def __init__(self,filename, framewidth, frametime):
        self.surface = pygame.image.load(filename)
        self.surface = self.surface.convert_alpha()
        self.frames = []
        x = 0
        while x < self.surface.get_width():
            newSurf = pygame.Surface((framewidth,self.surface.get_height()))
            newSurf = newSurf.convert_alpha()
            newSurf.fill((0,0,0,0))
            blitrect = pygame.rect.Rect(x,0,framewidth,self.surface.get_height())
            newSurf.blit(self.surface,(0,0),blitrect)
            x += framewidth
            self.frames.append(newSurf)
        self.index = 0
        self.img = self.frames[0]
        self.frametime = frametime
        self.framestart = pygame.time.get_ticks()
    def getFrame(self):
        if pygame.time.get_ticks() - self.framestart > self.frametime:
            self.img = self.getNextFrame()
        return self.img
    def getNextFrame(self):
        self.index += 1
        self.framestart = pygame.time.get_ticks()
        if self.index >= len(self.frames):
            self.index = 0
            return None
        return self.frames[self.index]
    def reset(self):
        self.index = 0
        self.img = self.frames[0]
        self.framestart = pygame.time.get_ticks()
