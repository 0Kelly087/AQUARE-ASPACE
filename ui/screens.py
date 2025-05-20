import pygame

class ScreenManager:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.transform.scale(pygame.image.load("ASETS/FONDOS/PGAME.png"),
                                                 (screen.get_width(), screen.get_height()))
        self.play_button_img = pygame.transform.scale(pygame.image.load("ASETS/FONDOS/PLAY.png"), (300, 150))
        self.play_button_rect = self.play_button_img.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        self.over_img = pygame.transform.scale(pygame.image.load("ASETS/FONDOS/GAMEOVER.png"), (600, 400))
        self.win_img = pygame.transform.scale(pygame.image.load("ASETS/FONDOS/GANASTE.png"), (600, 400))
        self.small_font = pygame.font.SysFont("comicsansms", 24)

    def show_start_screen(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.play_button_img, self.play_button_rect)
        info_text = self.small_font.render("Haz clic en PLAY para comenzar", True, (255, 255, 255))
        self.screen.blit(info_text, (self.screen.get_width() // 2 - info_text.get_width() // 2,
                                     self.play_button_rect.bottom + 10))

    def show_game_over(self):
        self.screen.blit(self.over_img, (self.screen.get_width() // 2 - 300, self.screen.get_height() // 2 - 200))

    def show_win_screen(self):
        self.screen.blit(self.win_img, (self.screen.get_width() // 2 - 300, self.screen.get_height() // 2 - 200))
