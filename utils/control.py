import pygame


class Control:
    events = []
    keys = []

    @staticmethod
    def update_events():
        Control.events = pygame.event.get()
        Control.keys = pygame.key.get_pressed()

    @staticmethod
    def check_press(key):
        for event in Control.events:
            if event.type == pygame.KEYDOWN and event.key == key:
                return True
        return False
