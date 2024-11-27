import pygame
from utils.scene_manager import Scene


class Map(Scene):
    def __init__(self, surface):
        self.surface = surface
        self.locations = ["basement"]
        self.selected_location = 0

    def update(self):
        self.surface.fill((0, 0, 0))
        font = pygame.font.Font(None, 74)
        text = font.render("Выберите локацию", True, (255, 255, 255))
        self.surface.blit(text, (100, 100))
        location_text = font.render(
            f"Локация: {self.locations[self.selected_location]}", True, (255, 255, 255)
        )
        self.surface.blit(location_text, (100, 200))

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.manager.change_scene(
                        self.locations[self.selected_location], 1
                    )

    def start_music(self):
        pygame.mixer.music.load("sound/main_music.mp3")
        pygame.mixer.music.play(-1)

