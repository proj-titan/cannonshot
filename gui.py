import sys
import pygame
import time
from random import *
from pygame.locals import *

class image():
    def __init__(self, surf, rect):
        self.surf = surf
        self.rect = rect

class gameobj():
    def __init__(self, img):
        self.rect = img.rect
        self.img = img
    #
    def draw(self, surf):
        surf.blit\
            ( self.img.surf
            , self.rect)
    #
    def collideall(self, other):
        return self.rect.collidelistall(other)

class cannon(gameobj):
    """docstring for cannon."""
    def __init__(self, img, shotpoint, cannonballimg):
        super(cannon, self).__init__(img)
        self.shotpoint = shotpoint
        self.cannonballimg = cannonballimg
    #
    def shot(self):
        return cannonball(self.cannonballimg)

class cannonball(gameobj):
    """docstring for cannonball.
        it is empty."""
