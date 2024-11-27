import pygame


class Control:
    @staticmethod
    def check_press(key):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == key:
                return True
        return False

