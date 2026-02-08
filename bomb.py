from math import floor
import pygame


class Bomb:
    def __init__(self, screen):
        self.screen = screen
        self.explode_on = False
        self.speed = 0.1
        self.delay = 0
        self.number_placed = 0
        self.number_left = 0
        self.max_bombs = 0
        self.positions = []
        self.data = (0, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 6, 6, 7)

    def level_update(self, level):
        self.max_bombs = int(self.data[level])
        self.number_placed = 0
        self.number_left = self.max_bombs

    def explode_bombs(self, grid_size, square_size, enemy):
        directions_amount = [(-square_size, -square_size), (0, -square_size), (square_size, -square_size), (-square_size, 0),
                             (square_size, 0), (-square_size, square_size), (0, square_size), (square_size, square_size)]
        # For Each Bomb
        for b in range(len(self.positions)):
            # Each Direction
            for q in range(0, 8):
                x_pos = self.positions[b][0]
                y_pos = self.positions[b][1]
                # Amount Of Times
                for e in range(0, floor(self.delay)):
                    x_pos += directions_amount[q][0]
                    y_pos += directions_amount[q][1]
                    # Updating canvas
                    if floor(self.delay) - 2 <= e <= floor(self.delay):
                        if ((grid_size * square_size) > x_pos >= 0) and ((square_size * grid_size) > y_pos >= 0):
                            pygame.draw.rect(self.screen, (255, 108, 0), pygame.Rect(x_pos, y_pos, square_size, square_size))
                            pygame.draw.rect(self.screen, (147, 149, 152), pygame.Rect(x_pos, y_pos, square_size, square_size), 2)
                            enemy.check(x_pos, y_pos)
        self.delay += self.speed if self.delay < grid_size + 1 else 0
        self.speed += (self.speed / 60)

    def update(self):
        if len(self.positions) > self.number_placed and self.positions:
            self.positions.pop(-1 * (len(self.positions) - self.number_placed))
            self.number_placed -= 1
        for k, bomb1 in enumerate(self.positions):
            for m, bomb2 in enumerate(self.positions):
                if bomb1 == bomb2 and k != m:
                    self.positions.pop(m)
                    self.number_placed -= 1
                    self.number_left += 1
        if self.number_left == 0:
            self.explode_on = True

    def place(self, current_pos):
        if self.number_placed < self.max_bombs and not self.explode_on:
            self.number_placed += 1
            self.number_left -= 1
            self.positions.append(current_pos)

    def remove(self):
        if self.number_left < self.max_bombs and not self.explode_on:
            self.number_left += 1
            self.number_placed -= 1
            self.positions.pop()
