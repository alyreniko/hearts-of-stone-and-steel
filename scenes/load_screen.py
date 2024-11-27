import pygame
import utils.variables as var
from classes.scene import Scene
from utils.scene_manager import SceneManager


class GameIntro(Scene):
    def __init__(self):
        self.background_music = None
        self.screen = var.SCREEN
        self.background_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.texts = [
            "Добро пожаловать в Sara!",
            "Разработчик: Хайдаров Диёр",
            "Приятной игры!"
        ]
        self.current_text_index = 0
        self.alpha = 0
        self.fade_in = True
        self.display_time = 0
        self.text_surface = None
        self.finished = False

    def render_text(self, text):
        font = pygame.font.Font(None, 48)
        text_surface = font.render(text, True, self.text_color)
        return text_surface.convert_alpha()

    def update(self):
        if self.finished:
            SceneManager.change_scene("main_menu")
            return

        var.SCREEN.fill(self.background_color)

        if self.display_time > 0:
            self.display_time -= 1
        else:
            if self.fade_in:
                self.alpha += 255 // var.FPS
                if self.alpha >= 255:
                    self.alpha = 255
                    self.fade_in = False
                    self.display_time = 30
            else:
                self.alpha -= 255 // var.FPS
                if self.alpha <= 0:
                    self.alpha = 0
                    self.fade_in = True
                    self.current_text_index += 1

                    if self.current_text_index >= len(self.texts):
                        self.finished = True
                        return

        if not self.text_surface or self.alpha == 0:
            self.text_surface = self.render_text(self.texts[self.current_text_index])

        self.text_surface.set_alpha(self.alpha)
        text_rect = self.text_surface.get_rect(center=(var.SCREEN_WIDTH // 2, var.SCREEN_HEIGHT // 2))
        var.SCREEN.blit(self.text_surface, text_rect)
