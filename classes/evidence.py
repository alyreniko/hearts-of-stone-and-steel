import pygame
import utils.variables as var
from classes.interaction import Interaction


class Evidence(Interaction):
    def __init__(self, x, y, width, height, image, evidence_name):
        super().__init__(x, y, width, height, image)
        self.fullscreen_image = pygame.transform.smoothscale(
            pygame.image.load(image).convert(), (width * 3, height * 3)
        )
        self.evidence_name = self.font.render(evidence_name, True, (255, 0, 5))
        self.width = width
        self.height = height

    def action(self):
        var.SCREEN.fill((0, 0, 0))
        var.SCREEN.blit(
            self.fullscreen_image,
            (1920 // 2 - self.width * 3 // 2, 1080 // 2 - self.height * 3 // 2),
        )
        var.SCREEN.blit(
            self.evidence_name,
            (
                1920 // 2 - self.evidence_name.get_width() // 2,
                1080 // 2 + self.height * 3 - self.evidence_name.get_height() // 2,
            ),
        )
        pygame.display.update()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    waiting = False
