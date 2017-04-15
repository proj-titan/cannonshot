import sys
import pygame
import time
from random import *
from pygame.locals import *
import gui
mpos = []

while True:
    clicked = False
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mpos = event.pos
        elif event.type == MOUSEBUTTONUP:
            clicked = True
    pygame.display.update()
