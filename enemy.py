from random import randint


class Enemy:
    def __init__(self):
        self.placed = False
        self.bombs_placing = 0
        self.enemy_size = 0
        self.grid_size = 0
        self.positions = []

    def collect_possible_values(self, squares_coords, amount: int) -> list:
        directions_amount = [(-self.enemy_size, -self.enemy_size), (0, -self.enemy_size),
                             (self.enemy_size, -self.enemy_size), (-self.enemy_size, 0), (self.enemy_size, 0),
                             (-self.enemy_size, self.enemy_size), (0, self.enemy_size),
                             (self.enemy_size, self.enemy_size)]
        directions = [randint(0, 7) for _ in range(amount)]
        all_squares = []
        # Amount Of Times
        for q in directions:
            x_pos = squares_coords[0]
            y_pos = squares_coords[1]
            possible_bombs = []
            # Check Version
            if q == 0:
                while ((((self.grid_size - 1) * self.enemy_size) >= x_pos > 0) and
                       (((self.grid_size - 1) * self.enemy_size) >= y_pos > 0)):
                    x_pos += directions_amount[q][0]
                    y_pos += directions_amount[q][1]
                    possible_bombs.append((x_pos, y_pos))
            if q == 1:
                while ((self.grid_size - 1) * self.enemy_size) >= y_pos > 0:
                    y_pos += directions_amount[q][1]
                    possible_bombs.append((x_pos, y_pos))
            if q == 2:
                while ((((self.grid_size - 1) * self.enemy_size) > x_pos >= 0) and
                       (((self.grid_size - 1) * self.enemy_size) >= y_pos > 0)):
                    x_pos += directions_amount[q][0]
                    y_pos += directions_amount[q][1]
                    possible_bombs.append((x_pos, y_pos))
            if q == 3:
                while ((self.grid_size - 1) * self.enemy_size) >= x_pos > 0:
                    x_pos += directions_amount[q][0]
                    possible_bombs.append((x_pos, y_pos))
            if q == 4:
                while ((self.grid_size - 1) * self.enemy_size) > x_pos >= 0:
                    x_pos += directions_amount[q][0]
                    possible_bombs.append((x_pos, y_pos))
            if q == 5:
                while ((((self.grid_size - 1) * self.enemy_size) >= x_pos > 0) and
                       (((self.grid_size - 1) * self.enemy_size) > y_pos >= 0)):
                    x_pos += directions_amount[q][0]
                    y_pos += directions_amount[q][1]
                    possible_bombs.append((x_pos, y_pos))
            if q == 6:
                while ((self.grid_size - 1) * self.enemy_size) > y_pos >= 0:
                    y_pos += directions_amount[q][1]
                    possible_bombs.append((x_pos, y_pos))
            if q == 7:
                while ((((self.grid_size - 1) * self.enemy_size) > x_pos >= 0) and
                       (((self.grid_size - 1) * self.enemy_size) > y_pos >= 0)):
                    x_pos += directions_amount[q][0]
                    y_pos += directions_amount[q][1]
                    possible_bombs.append((x_pos, y_pos))
            # Normal Version
            # while ((32 * 15) > x_pos > 0) and ((32 * 15) > y_pos > 0):
            #    x_pos += directions_amount[q][0]
            #    y_pos += directions_amount[q][1]
            #    possible_bombs.append((x_pos, y_pos))
            if not possible_bombs:
                continue
            if len(possible_bombs) > 2:
                all_squares.append(possible_bombs[randint(0, len(possible_bombs) - 1)])
            else:
                all_squares.append(possible_bombs[0])
        return all_squares

    def place(self, grid_size, sizeVar, max_bombs):
        self.enemy_size = sizeVar
        self.grid_size = grid_size
        self.bombs_placing = max_bombs
        for v in range(self.bombs_placing):
            num1 = randint(0, self.grid_size - 1)
            num2 = randint(0, self.grid_size - 1)
            nums = [(num1 * self.enemy_size), (num2 * self.enemy_size)]
            # Testing
            amount = randint(4, 8)
            for bomb in self.collect_possible_values(nums, amount):
                self.positions.append(bomb)
        self.placed = True

    def check(self, x_pos, y_pos):
        for enemy in self.positions:
            if enemy == (x_pos, y_pos):
                self.positions.remove(enemy)
