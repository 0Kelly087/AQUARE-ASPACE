from entities.entity import Entity
import pygame

class Bullet(Entity):
    def __init__(self, x, y):
        super().__init__("ASETS/FONDOS/BALA.png", 10, 25, x, y)
        self.speed = 12
        self.fired = False
        self.default_y = y

    def fire(self, x, y):
        self.fired = True
        self.rect.centerx = x
        self.rect.top = y

    def update(self, player):
        if self.fired:
            self.rect.y -= self.speed
            if self.rect.bottom < 0:
                self.reset(player)

    def reset(self, player):
        self.fired = False
        self.rect.top = player.rect.top
