from entities.entity import Entity
import pygame

class Player(Entity):
    def __init__(self, screen_width, screen_height):
        super().__init__("ASETS/AVATARS/CROQUI/5C.png", 150, 150,
                         x=screen_width // 2, y=screen_height - 170)
        self.speed = 8
        self.screen_width = screen_width
        self.default_x = self.rect.x

    def handle_input(self, event, bullet):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.rect.x -= self.speed
            elif event.key == pygame.K_RIGHT:
                self.rect.x += self.speed
            elif event.key == pygame.K_SPACE and not bullet.fired:
                bullet.fire(self.rect.centerx, self.rect.top)

    def update(self):
        self.rect.x = max(0, min(self.rect.x, self.screen_width - self.rect.width))

    def reset(self):
        self.rect.x = self.default_x
