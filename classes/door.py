from classes.interaction import Interaction
from utils.scene_manager import SceneManager
import pygame


class Door(Interaction):
    def __init__(self, x, y, width, height, image, target_scene):
        super().__init__(x, y, width, height, image)
        self.target_scene = target_scene

    def action(self):
        SceneManager.change_scene(self.target_scene)