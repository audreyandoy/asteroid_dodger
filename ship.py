import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("ship.png")
        self.scale = 0.5
        width = int(self.image.get_rect().width*self.scale)
        height = int(self.image.get_rect().height*self.scale)
        self.image = pygame.transform.smoothscale(
            self.image, (width, height)
        )
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(2,0)
