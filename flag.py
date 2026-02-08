import pygame


class Flag:
    def __init__(self):
        self.number_placed = 0
        self.positions = []

    def place(self, position):
        for i, value in enumerate(self.positions):
            if value == position:
                self.positions.remove(value)
                self.number_placed -= 1
                return
        self.positions.append(position)
        self.number_placed += 1

    def display(self, screen, sizeVar):
        if self.number_placed > 0:
            for i in range(0, self.number_placed):
                pygame.draw.rect(screen, (242, 0, 255), pygame.Rect(self.positions[i][0], self.positions[i][1],
                                                                    sizeVar, sizeVar))
                pygame.draw.rect(screen, (147, 149, 152), pygame.Rect(self.positions[i][0], self.positions[i][1],
                                                                      sizeVar, sizeVar), 2)
