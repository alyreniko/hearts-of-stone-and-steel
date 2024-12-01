import pygame
import utils.variables as var
from utils.control import Control
from classes.interaction import Interaction


class Player:
    def __init__(self):
        self.path = "assets/sprites/player/"
        self.images = [f"{self.path}{i}.png" for i in range(1, 8)]
        self.index = 0
        self.image = pygame.transform.scale(
            pygame.image.load(self.images[self.index]).convert_alpha(), (256, 256)
        )
        self.rect = self.image.get_rect()
        self.rect.center = (100, 920)
        self.speed = 10
        self.direction = "right"
        self.original_image = self.image
        self.frame_count = 0

    def update(self, bg_rect):
        if self.frame_count % 4 == 0:
            self.index = (self.index + 1) % len(self.images)
            self.image = pygame.transform.scale(
                pygame.image.load(self.images[self.index]).convert_alpha(), (256, 256)
            )
            if Control.keys[var.MOVE_LEFT]:
                if self.direction != "left":
                    self.direction = "left"
                self.image = pygame.transform.flip(self.image, True, False)
            elif Control.keys[var.MOVE_RIGHT]:
                if self.direction != "right":
                    self.direction = "right"
                self.image = pygame.transform.flip(self.image, False, False)
            else:
                self.direction = "idle"
                self.image = self.original_image
            self.frame_count = 0

        self.frame_count += 1

        if Control.keys[var.MOVE_LEFT]:
            self.rect.x -= self.speed

        elif Control.keys[var.MOVE_RIGHT]:
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

