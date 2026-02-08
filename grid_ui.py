import pygame
from random import randint


class Grid_UI:
    def __init__(self, screen, data):
        self.screen = screen
        self.game_end_delay = 0
        self.data = data
        self.winning_animation, self.losing_animation, self.finish_animation = data.define()

    def lose_screen(self):
        print("delay: " + str(self.game_end_delay))
        y = 0
        for j in range(1, 33):
            x = 0
            for i in range(1, 33):
                pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(x, y, 15, 15))
                pygame.draw.rect(self.screen, (15, 15, 15), pygame.Rect(x, y, 15, 15), 2)
                x += 15
            y += 15
        for i, value in enumerate(self.losing_animation):
            pygame.draw.rect(self.screen, (233, 58, 36), pygame.Rect(int(value[0]), int(value[1]), 15, 15))
            pygame.draw.rect(self.screen, (15, 15, 15), pygame.Rect(int(value[0]), int(value[1]), 15, 15), 2)
        # Game End
        self.game_end_delay += 0.1
        if self.game_end_delay >= 30:
            return True

    def win_screen(self):
        y = 0
        for j in range(1, 33):
            x = 0
            for i in range(1, 33):
                pygame.draw.rect(self.screen, (randint(0, 255), randint(0, 255), randint(0, 255)),
                                 pygame.Rect(x, y, 15, 15))
                pygame.draw.rect(self.screen, (15, 15, 15), pygame.Rect(x, y, 15, 15), 2)
                x += 15
            y += 15
        for i, value in enumerate(self.winning_animation):
            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(int(value[0]), int(value[1]), 15, 15))
            pygame.draw.rect(self.screen, (15, 15, 15), pygame.Rect(int(value[0]), int(value[1]), 15, 15), 2)
        self.game_end_delay += 0.1
        # Game End
        if self.game_end_delay >= 30:
            return True

    def game_complete_screen(self):
        y = 0
        for j in range(1, 33):
            x = 0
            for i in range(1, 33):
                pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(x, y, 15, 15))
                pygame.draw.rect(self.screen, (15, 15, 15), pygame.Rect(x, y, 15, 15), 2)
                x += 15
            y += 15
        for i, value in enumerate(self.finish_animation):
            pygame.draw.rect(self.screen, (255, 179, 0), pygame.Rect(int(value[0]), int(value[0]), 15, 15))
            pygame.draw.rect(self.screen, (15, 15, 15), pygame.Rect(int(value[0]), int(value[1]), 15, 15), 2)
        # Game End
        self.game_end_delay += 0.1
        if self.game_end_delay >= 30:
            return True

    def bomb_squares(self, bomb, square_size):
        for i in range(0, bomb.number_placed):
            if bomb.number_placed == 0:
                break
            pygame.draw.rect(self.screen, (43, 57, 144),
                             pygame.Rect(bomb.positions[i][0], bomb.positions[i][1], square_size, square_size))
            pygame.draw.rect(self.screen, (147, 149, 152),
                             pygame.Rect(bomb.positions[i][0], bomb.positions[i][1], square_size, square_size), 2)

    def enemy_squares(self, enemy, square_size):
        for e in range(len(enemy.positions)):
            pygame.draw.rect(self.screen, (233, 58, 36), pygame.Rect(enemy.positions[e][0], enemy.positions[e][1],
                                                                     square_size, square_size))
            pygame.draw.rect(self.screen, (147, 149, 152), pygame.Rect(enemy.positions[e][0], enemy.positions[e][1],
                                                                       square_size, square_size), 2)

    def grid_squares(self, grid_size, square_size):
        y = 0
        for j in range(1, (grid_size+1)):
            x = 0
            for i in range(1, (grid_size+1)):
                pygame.draw.rect(self.screen, (167, 169, 172), pygame.Rect(x, y, square_size, square_size))
                pygame.draw.rect(self.screen, (147, 149, 152), pygame.Rect(x, y, square_size, square_size), 2)
                x += square_size
            y += square_size

