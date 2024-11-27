import pygame
from classes.button import Button
from classes.scene import Scene
import utils.variables as var
from utils.scene_manager import SceneManager
from utils.music_manager import MusicManager


class MainMenu(Scene):
    def __init__(self):
        self.background = pygame.transform.smoothscale(
            pygame.image.load("assets/sprites/main_background.png").convert(),
            (var.SCREEN_WIDTH, var.SCREEN_HEIGHT)
        )
        self.background_music = "assets/sound/main_music.mp3"
        self.buttons = [
            Button("Играть", 150, 320, 300, 100, self.start_game),
            Button("Настройки", 150, 470, 300, 100, self.settings),
            Button("Выход", 150, 620, 300, 100, self.quit_game),
        ]

    def update(self):
        var.SCREEN.blit(self.background, (0, 0))
        for button in self.buttons:
            button.draw(var.SCREEN)

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in self.buttons:
                    if button.is_hover():
                        button.click()

    def start_game(self):
        SceneManager.change_scene("basement")

    def settings(self):
        SceneManager.change_scene("settings")

    def quit_game(self):
        pygame.quit()
        exit()

    def start_scene(self):
        super().start_scene()
