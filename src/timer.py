import pygame


class Timer():
    def __init__(self, duration):
        self.start = pygame.time.get_ticks()
        self.duration = duration
