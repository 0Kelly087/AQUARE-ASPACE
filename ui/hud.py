import pygame

class HUD:
    def __init__(self):
        self.font = pygame.font.SysFont("comicsansms", 36)
        self.garbage_icons = {
            i: pygame.transform.scale(pygame.image.load(f"ASETS/BASURAS/BASURA{i}.png"), (50, 50))
            for i in range(1, 9)
        }
        self.life_bar_width = 250
        self.life_bar_height = 30
        self.life_bar_x = 30
        self.life_bar_y = 640 - 70

    def draw(self, screen, score, kills_by_type, time_left):
        self.draw_score(screen, score, kills_by_type)
        self.draw_life_bar(screen, score)
        self.draw_timer(screen, time_left)

    def draw_score(self, screen, score, kills_by_type):
        score_text = self.font.render(f"SCORE: {score}", True, (255, 255, 255))
        screen.blit(score_text, (20, 20))
        x_offset = 200
        for i in range(1, 9):
            screen.blit(self.garbage_icons[i], (x_offset, 10))
            count_text = self.font.render(str(kills_by_type[i]), True, (255, 255, 255))
            screen.blit(count_text, (x_offset + 55, 15))
            x_offset += 95

    def draw_life_bar(self, screen, score):
        percentage = min(score / 50, 1)
        red = int(255 * (1 - percentage))
        green = int(255 * percentage)
        color = (red, green, 0)
        pygame.draw.rect(screen, (50, 50, 50),
                         (self.life_bar_x, self.life_bar_y, self.life_bar_width, self.life_bar_height), border_radius=8)
        pygame.draw.rect(screen, color,
                         (self.life_bar_x, self.life_bar_y, self.life_bar_width * percentage, self.life_bar_height),
                         border_radius=8)

    def draw_timer(self, screen, time_left):
        timer_text = self.font.render(f"TIEMPO: {time_left}", True, (255, 255, 255))
        screen.blit(timer_text, (screen.get_width() - timer_text.get_width() - 30, screen.get_height() - 70))
