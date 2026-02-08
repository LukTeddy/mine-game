import pygame


class Player:
    def __init__(self, screen, tile_size, tile_amount, bomb, flag):
        self.screen = screen
        self.tile_size = tile_size
        self.tile_amount = tile_amount
        self.pressed = 0
        self.pos_x = 0
        self.pos_y = 0
        self.active = True
        self.bomb = bomb
        self.flag = flag

    def key_input(self, event_type):
        # Make it so you can hold keys
        hold_frame = 10
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
            self.pressed += 1
            if self.pos_y != 0 and (self.pressed == 1 or self.pressed > hold_frame):
                self.pos_y -= self.tile_size
        elif key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
            self.pressed += 1
            if self.pos_x != 0 and (self.pressed == 1 or self.pressed > hold_frame):
                self.pos_x -= self.tile_size
        elif key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
            self.pressed += 1
            if self.pos_y != ((self.tile_amount-1) * self.tile_size) and (self.pressed == 1 or self.pressed > hold_frame):
                self.pos_y += self.tile_size
        elif key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
            self.pressed += 1
            if self.pos_x != ((self.tile_amount-1) * self.tile_size) and (self.pressed == 1 or self.pressed > hold_frame):
                self.pos_x += self.tile_size
        else:
            self.pressed = 0
        if event_type == pygame.KEYDOWN:
            if key_pressed[pygame.K_SPACE] or key_pressed[pygame.K_RETURN]:
                current_pos_x = self.pos_x
                current_pos_y = self.pos_y
                current_pos = [current_pos_x, current_pos_y]
                self.bomb.place(current_pos)
            if key_pressed[pygame.K_f]:
                current_pos_x = self.pos_x
                current_pos_y = self.pos_y
                current_pos = [current_pos_x, current_pos_y]
                self.flag.place(current_pos)
            if key_pressed[pygame.K_r] or key_pressed[pygame.K_BACKSPACE]:
                self.bomb.remove()

    def draw(self):
        if self.active:
            pygame.draw.rect(self.screen, (38, 215, 239),
                             pygame.Rect(self.pos_x, self.pos_y, self.tile_size, self.tile_size))
            pygame.draw.rect(self.screen, (147, 149, 152),
                             pygame.Rect(self.pos_x, self.pos_y, self.tile_size, self.tile_size), 2)