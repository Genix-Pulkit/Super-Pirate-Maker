import pygame


class Timer:
    def __init__(self, duration):
        self.duration = duration
        self.active = False
        self.start_timer = 0

    def activate(self):
        self.active = True
        self.start_timer = pygame.time.get_ticks()

    def deactivate(self):
        self.active = False
        self.start_timer = 0

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.start_timer >= self.duration:
            self.deactivate()
