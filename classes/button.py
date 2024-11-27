import pygame


class Button:
    def __init__(self, text, x, y, width, height, action=None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.action = action
        self.font = pygame.font.Font('assets/fonts/Catacombs.ttf', 48)

    def draw(self, surface):
        pygame.draw.rect(
            surface,
            (0, 0, 0) if self.is_hover() else (255, 255, 255),
            self.rect
        )
        self.text_surface = self.font.render(self.text, True, (155, 0, 0))
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
        surface.blit(self.text_surface, self.text_rect)

    def is_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)

    def click(self):
        if self.action:
            self.action()
