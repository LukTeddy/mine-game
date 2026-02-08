import pygame


class Audio:
    def __init__(self, name, volume):
        self.name = "assets/audio/" + name
        self.audio = pygame.mixer.Sound(self.name)
        self.audio.set_volume(volume)

    def play(self, times=-1):
        self.audio.play(loops=times)

    def stop(self):
        self.audio.stop()
