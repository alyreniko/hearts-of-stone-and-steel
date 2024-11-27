import pygame
import utils.variables as var
from utils.camera import Camera
from classes.scene import Scene
from utils.music_manager import MusicManager
from classes.evidence import Evidence
from classes.door import Door


class Basement(Scene):
    def __init__(self, player, background):
        super().__init__(player, background, 3000, 1080)
        self.evidence = Evidence(500, 900, 100, 100, "assets/sprites/evidence.png", "Улика")
        self.door = Door(800, 900, 100, 200, "assets/sprites/door.png", "bar")
        self.door1 = Door(1200, 900, 100, 200, "assets/sprites/door.png", "game")
        self.background_music = "assets/sound/sound_game.mp3"
        self.last_player_pos = (100, 900)

    def update(self):
        bg_rect = self.background.get_rect()
        screen_rect = self.camera.apply(bg_rect)
        var.SCREEN.blit(self.background, screen_rect)

        self.last_player_pos = self.player.rect.center

        self.player.update(bg_rect)
        self.camera.update(self.player.rect)


        self.evidence.update(self.player.rect, var.SCREEN, self.camera)
        self.door.update(self.player.rect, var.SCREEN, self.camera)
        self.door1.update(self.player.rect, var.SCREEN, self.camera)

        var.SCREEN.blit(self.player.image, self.camera.apply(self.player.rect))

    def start_scene(self):
        self.player.reset_position(*self.last_player_pos)
        super().start_scene()

    def handle_event(self):
        super().handle_event()

