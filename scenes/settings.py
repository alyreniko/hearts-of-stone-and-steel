import pygame

import utils.variables as var
from classes.button import Button
from classes.scene import Scene
from utils.control import Control
from utils.scene_manager import SceneManager


class Settings(Scene):
    def __init__(self):
        self.background = pygame.transform.smoothscale(
            pygame.image.load("assets/sprites/main_background.png").convert(),
            (1920, 1080)
        )
        self.background_music = "assets/sound/main_music.mp3"
        self.buttons = [
            Button(
                "Звук " + ("ВКЛ" if var.MUSIC_VOLUME > 0 else "ВЫКЛ"),
                150, 170, 300, 100, self.param1
            ),
            Button("Параметр", 150, 320, 300, 100, self.param),
            Button("Параметр", 150, 470, 300, 100, self.param),
            Button("Параметр", 150, 620, 300, 100, self.param),
            Button("Назад", 150, 770, 300, 100, self.param),
        ]

    def update(self):
        var.SCREEN.blit(self.background, (0, 0))
        for button in self.buttons:
            button.draw(var.SCREEN)

    def handle_event(self):
        for event in Control.events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in self.buttons:
                    if button.is_hover():
                        button.click()
            if Control.check_press(pygame.K_ESCAPE):
                SceneManager.change_scene("main_menu")

    def param(self):
        SceneManager.change_scene("main_menu")

    def param1(self):
        if var.MUSIC_VOLUME < 1:
            var.MUSIC_VOLUME = 1
        else:
            var.MUSIC_VOLUME = 0
        pygame.mixer.music.set_volume(var.MUSIC_VOLUME)
        self.buttons[0].text = "Звук " + ("ВКЛ" if var.MUSIC_VOLUME > 0 else "ВЫКЛ")

