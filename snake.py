import pygame
from pygame.locals import *
from sys import exit

## VALUES ##

# window title
window_title = "Snake!"

# screen values
width = 500
height = 500

## CODE ##

# set title
pygame.display.set_caption(window_title)

# starts code
pygame.init()
screen = pygame.display.set_mode((width,height))

# loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()