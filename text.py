import pygame


class Text:
    def __init__(self, screen):
        self.screen = screen
        self.font_type = None
        self.size = int

    def font(self, name, size):
        self.font_type = "assets/font/" + name
        self.size = size
        return pygame.font.Font(self.font_type, self.size)

    def draw(self, position, colour, font, text):
        text = font.render(text, False, colour)
        text_rect = text.get_rect(center=position)
        self.screen.blit(text, text_rect)
