import pygame
import utils.variables as var
from utils.camera import Camera
from classes.scene import Scene
from utils.music_manager import MusicManager
from classes.evidence import Evidence
from classes.door import Door
from utils.dialog import DialogWindow
from entity.npc_male_police import NPCMalePolice

class Basement(Scene):
    def __init__(self, player, background):
        super().__init__(player, background, 3000, 1080)
        self.evidence = Evidence(500, 900, 100, 100, "assets/sprites/evidence.png", "Улика")
        self.door = Door(900, 900, 100, 200, "assets/sprites/door.png", "bar")
        self.door1 = Door(1200, 900, 100, 200, "assets/sprites/door.png", "game")
        self.background_music = "assets/sound/sound_game.mp3"
        self.last_player_pos = (100, 900)
        self.dialog_window = DialogWindow(var.SCREEN_WIDTH, var.SCREEN_HEIGHT, "file.txt")
        self.npc = NPCMalePolice(200, 900, 256, 256, "assets/sprites/player/open_door", 16)

    def update(self):
        self.last_player_pos = self.player.rect.center

        self.camera.update(self.player.rect)

        player_rect = self.camera.apply(self.player.rect)
        
        bg_rect = self.background.get_rect()
        screen_rect = self.camera.apply(bg_rect)
        var.SCREEN.blit(self.background, screen_rect)

        self.evidence.update(self.player.rect, var.SCREEN, self.camera)
        self.door.update(self.player.rect, var.SCREEN, self.camera)
        self.door1.update(self.player.rect, var.SCREEN, self.camera)
        self.npc.update(self.player.rect, self.camera)

        self.player.update(bg_rect)
        var.SCREEN.blit(self.player.image, player_rect)

        self.npc.dialog.update()

    def start_scene(self):
        super().start_scene()
        self.player.reset_position(*self.last_player_pos)

    def handle_event(self):
        super().handle_event()

