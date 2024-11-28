import pygame
import utils.variables as var
from utils.music_manager import MusicManager
from utils.camera import Camera
from utils.control import Control
from utils.scene_manager import SceneManager


class Scene:
    def __init__(self, player, background, map_width, map_height):
        self.player = player
        self.background_music = None
        self.background = pygame.transform.smoothscale(
            pygame.image.load(background).convert(), (map_width, map_height)
        )
        self.camera = Camera(
            var.SCREEN.get_width(), var.SCREEN.get_height(), map_width, map_height
        )
        self.last_player_pos = (0, 0)

    def update(self):
        pass

    def handle_event(self):
        if Control.check_press(pygame.K_ESCAPE):
            SceneManager.change_scene("main_menu")

    def start_scene(self):
        MusicManager.changeMusic(self.background_music)
