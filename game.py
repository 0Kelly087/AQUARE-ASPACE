import pygame
from entities.player import Player
from entities.enemy import Enemy
from entities.bullet import Bullet
from ui.hud import HUD
from ui.screens import ScreenManager
import random

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width, self.screen_height = 1000, 640
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Aquare Space")
        pygame.display.set_icon(pygame.image.load("ASETS/BASURAS/BASURA1.png"))

        self.background = pygame.transform.scale(pygame.image.load("ASETS/FONDOS/PGAME.png"),
                                                 (self.screen_width, self.screen_height))
        pygame.mixer.music.load("ASETS/SONGS/1S.mp3")

        self.player = Player(self.screen_width, self.screen_height)
        self.enemies = [Enemy(self.screen_width) for _ in range(12)]
        self.bullet = Bullet(self.player.rect.centerx, self.player.rect.top)
        self.hud = HUD()
        self.screens = ScreenManager(self.screen)

        self.clock = pygame.time.Clock()
        self.running = True
        self.score = 0
        self.kills_by_type = {i: 0 for i in range(1, 9)}
        self.start_ticks = 0

        self.state = "start"  # start, play, win, gameover

    def run(self):
        while self.running:
            self.handle_events()

            if self.state == "start":
                self.screens.show_start_screen()
            elif self.state == "play":
                self.update()
                self.draw()
            elif self.state == "win":
                self.screens.show_win_screen()
            elif self.state == "gameover":
                self.screens.show_game_over()

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if self.state == "start":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.screens.play_button_rect.collidepoint(event.pos):
                        self.state = "play"
                        pygame.mixer.music.play(-1)
                        self.start_ticks = pygame.time.get_ticks()

            elif self.state == "play":
                self.player.handle_input(event, self.bullet)

            elif self.state in ["win", "gameover"]:
                if event.type == pygame.KEYDOWN:
                    self.reset()

    def update(self):
        self.player.update()
        self.bullet.update(self.player)

        for enemy in self.enemies:
            enemy.update()
            if enemy.rect.bottom > self.screen_height - 160:
                self.state = "gameover"
            if self.bullet.rect.colliderect(enemy.rect):
                self.bullet.reset(self.player)
                self.score += 1
                self.kills_by_type[enemy.enemy_type] += 1
                enemy.reset_position()

        if self.score >= 50:
            self.state = "win"

        remaining_time = max(0, 60 - (pygame.time.get_ticks() - self.start_ticks) // 1000)
        if remaining_time <= 0 and self.score < 50:
            self.state = "gameover"

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.player.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)
        if self.bullet.fired:
            self.bullet.draw(self.screen)

        self.hud.draw(self.screen, self.score, self.kills_by_type,
                      60 - (pygame.time.get_ticks() - self.start_ticks) // 1000)

    def reset(self):
        self.player.reset()
        self.enemies = [Enemy(self.screen_width) for _ in range(12)]
        self.bullet.reset(self.player)
        self.score = 0
        self.kills_by_type = {i: 0 for i in range(1, 9)}
        self.start_ticks = pygame.time.get_ticks()
        self.state = "play"
