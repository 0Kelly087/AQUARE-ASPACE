from entities.entity import Entity
import pygame
import random

class Enemy(Entity):
    def __init__(self, screen_width):
        self.screen_width = screen_width
        self.enemy_type = random.randint(1, 8)
        image_path = f"ASETS/BASURAS/BASURA{self.enemy_type}.png"
        x = random.randint(0, screen_width - 80)
        y = random.randint(50, 150)
        super().__init__(image_path, 80, 80, x, y)
        self.x_change = 3
        self.y_change = 40

    def update(self):
        self.rect.x += self.x_change
        if self.rect.left <= 0 or self.rect.right >= self.screen_width:
            self.x_change *= -1
            self.rect.y += self.y_change

    def reset_position(self):
        self.enemy_type = random.randint(1, 8)
        self.image = pygame.transform.scale(pygame.image.load(f"ASETS/BASURAS/BASURA{self.enemy_type}.png"), (80, 80))
        self.rect.x = random.randint(0, self.screen_width - 80)
        self.rect.y = random.randint(50, 150)
