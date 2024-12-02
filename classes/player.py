import pygame
import utils.variables as var
from utils.control import Control
from classes.interaction import Interaction

class Player:
    def __init__(self):
        self.path = "assets/sprites/player/"
        self.walk_images = [f"{self.path}/walk/{i}.png" for i in range(1, 8)]
        self.walk_turn_images = [f"{self.path}/walk_turn/{i}.png" for i in range(1, 7)]
        self.idle_images = [f"{self.path}/idle/{i}.png" for i in range(1, 20)]
        self.idle_turn_images = [f"{self.path}/idle_turn/{i}.png" for i in range(1, 11)]
        self.walk_index = 0
        self.walk_turn_index = 0
        self.idle_index = 0
        self.idle_turn_index = 0
        self.image = pygame.transform.scale(
            pygame.image.load(self.idle_images[self.idle_index]).convert_alpha(), (256, 256)
        )
        self.rect = self.image.get_rect()
        self.rect.center = (100, 920)
        self.speed = 10
        self.direction = "right"
        self.state = "idle"
        self.is_turning = False
        self.frame_count = 0

    def update(self, bg_rect):
        if not self.is_turning:
            if Control.keys[var.MOVE_LEFT]:
                if self.direction != "left":
                    self.is_turning = True
                    self.new_direction = "left"
                    self.turn_index = 0
                else:
                    self.state = "walk"
                    self.rect.x -= self.speed
            elif Control.keys[var.MOVE_RIGHT]:
                if self.direction != "right":
                    self.is_turning = True
                    self.new_direction = "right"
                    self.turn_index = 0
                else:
                    self.state = "walk"
                    self.rect.x += self.speed
            else:
                self.state = "idle"

        if self.frame_count % 4 == 0:
            if self.is_turning:
                turn_images = self.walk_turn_images if self.state == "walk" else self.idle_turn_images
                self.image = pygame.transform.scale(
                    pygame.image.load(turn_images[self.turn_index]).convert_alpha(), (256, 256)
                )
                if self.new_direction == "left":
                    self.image = pygame.transform.flip(self.image, True, False)
                self.turn_index += 1
                if self.turn_index >= len(turn_images):
                    self.turn_index = 0
                    self.is_turning = False
                    self.direction = self.new_direction
            else:
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
                if self.direction == "left":
                    self.image = pygame.transform.flip(self.image, True, False)

            self.frame_count = 0

        self.frame_count += 1

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
