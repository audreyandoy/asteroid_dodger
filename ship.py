import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("ship.png")
        self.scale = 1
        width = int(self.image.get_rect().width*self.scale)
        height = int(self.image.get_rect().height*self.scale)
        self.image = pygame.transform.smoothscale(
            self.image, (width, height)
        )
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(2,0)

    def update(self):
        self.rect.move_ip(self.speed)
        screen_info = pygame.display.Info()
        if self.rect.right > screen_info.current_w:
            self.rect.right = screen_info.current_w
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > screen_info.current_h:
            self.rect.bottom = screen_info.current_h
        if self.rect.top < 0:
            self.rect.top = 0

    def checkReset(self, endPos):
        return self.rect.right >= endPos

    def reset(self, pos):
        self.rect.center = pos
        
