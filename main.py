import pygame
import utils.variables as var

# from scenes.map import Map
from scenes.settings import Settings
from scenes.main_menu import MainMenu
from scenes.load_screen import GameIntro

from utils.scene_manager import SceneManager

from classes.player import Player

from locations.bar import Bar
from locations.basement import Basement


def main():
    pygame.init()
    clock = pygame.time.Clock()

    pygame.display.set_caption("Sara")

    player = Player()

    SceneManager.add_scene("load_screen", GameIntro())
    SceneManager.add_scene("main_menu", MainMenu())
    SceneManager.add_scene("settings", Settings())
    SceneManager.add_scene(
        "basement", Basement(player, "assets/sprites/basement.png")
    )
    # SceneManager.add_scene("map", Map(screen))
    SceneManager.add_scene("bar", Bar(player, "assets/sprites/bar.png"))
    SceneManager.add_scene("game", Bar(player, "assets/sprites/game.png"))

    SceneManager.change_scene("main_menu")    # временно пропустил заставку, позже поставить "load_screen"

    pygame.mixer.music.set_volume(var.MUSIC_VOLUME)

    # Главный цикл
    while True:
        var.KEYS = pygame.key.get_pressed()
        # var.EVENTS = pygame.event.get()

        SceneManager.update()
        SceneManager.handle_event()

        for event in var.EVENTS:
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.flip()
        clock.tick(var.FPS)


if __name__ == "__main__":
    main()

