import pygame

class Entity:
    def __init__(self, image_path, width, height, x=0, y=0):
        self.image = pygame.transform.scale(pygame.image.load(image_path), (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
