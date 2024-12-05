import pygame
import utils.variables as var
from utils.control import Control

pygame.font.init()


class Interaction:
    def __init__(self, x, y, width, height, image):
        self.image = pygame.transform.smoothscale(
            pygame.image.load(image).convert(), (width, height)
        )
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.font = pygame.font.Font("assets/fonts/Catacombs.ttf", 80)
        self.text = self.font.render('E', True, (0, 0, 255))

    def update(self, player_rect, screen, camera):
        interaction_rect = camera.apply(self.rect)
        var.SCREEN.blit(self.image, interaction_rect)

        collide = self.rect.colliderect(player_rect)
        if collide:
            text_pos = (
                interaction_rect.center[0] - (self.text.get_width() // 2),
                interaction_rect.center[1] - self.image.get_height() - 50
            )
            var.SCREEN.blit(self.text, text_pos)
            if Control.check_press(var.INTERACT):
                self.action()

