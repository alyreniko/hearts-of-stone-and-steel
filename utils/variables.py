import pygame

FPS = 30
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)

MUSIC_VOLUME = 0

MOVE_LEFT = pygame.K_LEFT
MOVE_RIGHT = pygame.K_RIGHT
INTERACT = pygame.K_e

KEYS = pygame.key.get_pressed()
EVENTS = pygame.event.get()
