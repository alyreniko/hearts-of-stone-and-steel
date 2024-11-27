import pygame
from utils.scene_manager import Scene, SceneManager
from classes.player import Player


class Game(Scene):
    def __init__(self, surface):
        self.surface = surface
        self.player = Player(400, 400, surface)

    def update(self):
        self.surface.fill((100, 100, 100))
        pygame.draw.rect(self.surface, (255, 255, 100), (100, 100, 100, 100))
        self.player.update()
        self.player.handle_event()

    def start_music(self):
        pygame.mixer.music.load("sound/sound_game.mp3")
        pygame.mixer.music.play(-1)

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.manager.change_scene("menu", 1)

