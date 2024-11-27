import pygame
import utils.variables as var
from classes.interaction import Interaction


class Player:
    def __init__(self):
        self.image = pygame.transform.smoothscale(
            pygame.image.load("assets/sprites/player/player.png").convert(), (100, 200)
        )
        self.rect = self.image.get_rect()
        self.rect.center = (100, 920)
        self.speed = 10
        self.direction = "right"
        self.original_image = self.image

    def update(self, bg_rect):
        if var.KEYS[var.MOVE_LEFT]:
            if self.direction != "left":
                self.direction = "left"
                self.image = pygame.transform.flip(self.original_image, True, False)
            self.rect.x -= self.speed

        elif var.KEYS[var.MOVE_RIGHT]:
            if self.direction != "right":
                self.direction = "right"
                self.image = pygame.transform.flip(self.original_image, False, False)
            self.rect.x += self.speed

        if self.rect.left < bg_rect.left:
            self.rect.left = bg_rect.left
        if self.rect.right > bg_rect.right:
            self.rect.right = bg_rect.right
        if self.rect.top < bg_rect.top:
            self.rect.top = bg_rect.top
        if self.rect.bottom > bg_rect.bottom:
            self.rect.bottom = bg_rect.bottom

    def reset_position(self, x, y):
        self.rect.center = (x, y)
