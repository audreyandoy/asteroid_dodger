import pygame
import random
from pygame.locals import *
import sys
from ship import Ship

pygame.init()

# screen display
screen_info = pygame.display.Info()
# set width and height of the screen
screen_size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
color = (0, 127, 255)

# create player 
player = Ship((20,200))

def main():
    clock.tick(60)
    screen.fill(color)
    screen.blit(player.image, player.rect)
    pygame.display.flip()

if __name__ == '__main__':
    main()