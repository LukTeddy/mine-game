import pygame


class Button:
    def __init__(self, screen, img):
        self.screen = screen
        self.image = "assets/sprites/" + img
        self.image = pygame.image.load(self.image).convert_alpha()
        self.image_rect = None
        self.clicked = False

    def draw(self, x_pos, y_pos, width=None, height=None):
        if width is not None and height is not None:
            print("scale")
        self.image_rect = self.image.get_rect(center=(x_pos, y_pos))
        self.screen.blit(self.image, self.image_rect)

    def check_clicked(self):
        mouse = pygame.mouse.get_pos()
        if self.image_rect.collidepoint(mouse):
            return True
