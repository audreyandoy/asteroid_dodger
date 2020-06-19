import pygame
import random
from pygame.locals import *
import sys
from ship import Ship
from asteroid import Asteroid

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

# setup game variables
NumLevels = 4
Level = 1

asteroids = pygame.sprite.Group()
asteroid_count = 3

def init():
    global asteroids, asteroid_count
    player.reset((20, 200))
    asteroids.empty()
    asteroid_count += 3
    for i in range(asteroid_count):
        asteroids.add(
            Asteroid(
                # pos (x,y)
                (
                    random.randint(50, width-50),
                    random.randint(50, height-50)
                ),
                #scale
                random.choice([0.07, 0.08, 0.09])
            )
        )

def win():
    font = pygame.font.SysFont(None, 70)
    text = font.render("You escaped!!", True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (width // 2, height // 2)
    while True:
        clock.tick(60)
        screen.fill(color)
        screen.blit(text, text_rect)
        pygame.display.flip()


def main():
    global Level, NumLevels, asteroids

    init()

    while Level < NumLevels:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.speed[0] = 10
                if event.key == pygame.K_LEFT:
                    player.speed[0] = -10
                if event.key == pygame.K_UP:
                    player.speed[1] = -10
                if event.key == pygame.K_DOWN:
                    player.speed[1] = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.speed[0] = 0
                if event.key == pygame.K_LEFT:
                    player.speed[0] = 0
                if event.key == pygame.K_UP:
                    player.speed[1] = 0
                if event.key == pygame.K_DOWN:
                    player.speed[1] = 0

        # check for collision 
        player_hit = pygame.sprite.spritecollide(player, asteroids, False)

        if player.checkReset(width):
            Level += 1
            init()
            print(Level)
        elif player_hit:
            player.reset((20, 200))
        
        # draw sprites and add colors to screen, UI
        player.update()
        asteroids.update()
        screen.fill(color)
        asteroids.draw(screen)
        screen.blit(player.image, player.rect)
        pygame.display.flip()

    win()

if __name__ == '__main__':
    main()