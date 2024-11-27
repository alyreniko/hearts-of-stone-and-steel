import pygame
import utils.variables as var
from utils.camera import Camera
from utils.music_manager import MusicManager


class SceneManager:
    _scenes = {}
    _current_scene = None

    @staticmethod
    def add_scene(name, scene):
        SceneManager._scenes[name] = scene

    @staticmethod
    def change_scene(name):
        if name in SceneManager._scenes:
            SceneManager._current_scene = SceneManager._scenes[name]
            SceneManager._current_scene.start_scene()

    @staticmethod
    def handle_event():
        if SceneManager._current_scene:
            SceneManager._current_scene.handle_event()

    @staticmethod
    def update():
        if SceneManager._current_scene:
            SceneManager._current_scene.update()

