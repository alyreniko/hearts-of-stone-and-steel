import pygame
import utils.variables as var
from utils.control import Control
from classes.interaction import Interaction


class Player:
    def __init__(self):
        self.path = "assets/sprites/player/"
        self.walk_images = [f"{self.path}/walk/{i}.png" for i in range(1, 8)]
        self.idle_images = [f"{self.path}/idle/{i}.png" for i in range(1, 20)]
        self.walk_index = 0
        self.idle_index = 0
        self.image = pygame.transform.scale(
            pygame.image.load(self.idle_images[self.idle_index]).convert_alpha(), (256, 256)
        )
        self.rect = self.image.get_rect()
        self.rect.center = (100, 920)
        self.speed = 10
        self.direction = "right"
        self.state = "idle"
        self.original_image = self.image
        self.frame_count = 0

    def update(self, bg_rect):
        if self.frame_count % 4 == 0:
            if self.state == "idle":
                self.image = pygame.transform.scale(
                    pygame.image.load(self.idle_images[self.idle_index]).convert_alpha(), (256, 256)
                )
                self.idle_index = (self.idle_index + 1) % len(self.idle_images)
            elif self.state == "walk":
                self.image = pygame.transform.scale(
                    pygame.image.load(self.walk_images[self.walk_index]).convert_alpha(), (256, 256)
                )
                self.walk_index = (self.walk_index + 1) % len(self.walk_images)
            if Control.keys[var.MOVE_LEFT]:
                self.state = "walk"
                self.direction = "left"
                self.image = pygame.transform.flip(self.image, True, False)
            elif Control.keys[var.MOVE_RIGHT]:
                self.state = "walk"
                self.direction = "right"
            else:
                self.state = "idle"
                if self.direction == "left":
                    self.image = pygame.transform.flip(self.image, True, False)
                    # self.direction = "right"
                elif self.direction == "right":
                    self.image = pygame.transform.flip(self.image, False, False)
                    # self.direction = "left"
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