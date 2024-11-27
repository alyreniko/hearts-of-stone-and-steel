import pygame

class Camera:
    def __init__(self, screen_width, screen_height, map_width, map_height):
        self.offset = pygame.Vector2(0, 0)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.map_width = map_width
        self.map_height = map_height
        self.smoothness = 0.05

    def update(self, target_rect):
        target_offset_x = target_rect.centerx - self.screen_width // 2
        self.offset.x += (target_offset_x - self.offset.x) * self.smoothness
        self.offset.x = max(0, min(self.offset.x, self.map_width - self.screen_width))

    def apply(self, rect):
        return rect.move(-self.offset.x, -self.offset.y)