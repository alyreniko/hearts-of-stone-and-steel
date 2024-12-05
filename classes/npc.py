import pygame
import utils.variables as var
from classes.interaction import Interaction
from utils.control import Control


class NPC():
    def __init__(self, x, y, width, height, path, last_image_number):
        self.path = path
        self.width, self.height = width, height
        self.images = [
            pygame.transform.scale(
                pygame.image.load(f"{self.path}/{i}.png").convert_alpha(), (width, height)
            ) for i in range(1, last_image_number)
        ]
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.font = pygame.font.Font("assets/fonts/Catacombs.ttf", 80)
        self.text = self.font.render('E', True, (0, 0, 255))
        self.frame_count = 0

    def update(self, player, camera):
        if self.frame_count % 4 == 0:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]
        
        self.frame_count += 1

        interaction_rect = camera.apply(self.rect)
        var.SCREEN.blit(self.image, interaction_rect)

        collide = self.rect.colliderect(player)
        if collide:
            text_pos = (
                interaction_rect.center[0] - (self.text.get_width() // 2),
                interaction_rect.center[1] - self.image.get_height() - 50
            )
            var.SCREEN.blit(self.text, text_pos)
            if Control.check_press(var.INTERACT):
                self.action()