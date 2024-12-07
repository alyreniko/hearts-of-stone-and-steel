import pygame
import utils.variables as var

# from scenes.map import Map
from scenes.settings import Settings
from scenes.main_menu import MainMenu
from scenes.load_screen import GameIntro

from utils.control import Control
from utils.scene_manager import SceneManager

from classes.player import Player

from locations.bar import Bar
from locations.game import Game
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
    SceneManager.add_scene("game", Game(player, "assets/sprites/game.png"))

    SceneManager.change_scene("main_menu")    # временно пропустил заставку, позже поставить "load_screen"

    pygame.mixer.music.set_volume(var.MUSIC_VOLUME)

    count_frame = 0
    count_time = 0
    count_time_minute = 0
    # Главный цикл
    while True:
        if SceneManager._current_scene == var.CURRENT_LOCATION:
            count_frame += 1
            count_time = count_frame // var.FPS
            hours = count_time // 60
            minutes = count_time % 60
            formatted_time = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}"
            print(f"Пройденное время: {formatted_time}")
    
        Control.update_events()

        SceneManager.update()
        SceneManager.handle_event()

        for event in Control.events:
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.USEREVENT + 1:
                count_time += 1

        pygame.display.flip()
        clock.tick(var.FPS)


if __name__ == "__main__":
    main()

