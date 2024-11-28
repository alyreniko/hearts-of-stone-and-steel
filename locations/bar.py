import pygame
import utils.variables as var
from utils.camera import Camera
from classes.scene import Scene
# from utils.scene_manager import Scene
from classes.evidence import Evidence
from classes.door import Door


class Bar(Scene):
    def __init__(self, player, background):
        super().__init__(player, background, 1000, 600)
        self.evidence = Evidence(700, 900, 100, 100,
                                 "assets/sprites/evidence.png", "Улика в Баре")
        self.player_tp = False
        self.door = Door(1000, 900, 100, 200,
                         "assets/sprites/door.png", "basement")

    def update(self):
        self.camera.update(self.player.rect)

        player_rect = self.camera.apply(self.player.rect)
        bg_rect = self.background.get_rect()
        bg_rect.center = var.SCREEN.get_rect().center
        bg_rect.bottom = var.SCREEN.get_rect().bottom
        var.SCREEN.blit(self.background, bg_rect)

        self.evidence.update(self.player.rect, var.SCREEN, self.camera)
        self.door.update(self.player.rect, var.SCREEN, self.camera)

        self.player.update(bg_rect)

        var.SCREEN.blit(self.player.image, player_rect)

    def start_scene(self):
        self.player.reset_position(1000, 900)

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.manager.change_scene("menu", 0)

