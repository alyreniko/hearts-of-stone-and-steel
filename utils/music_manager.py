import pygame

pygame.mixer.init()


class MusicManager:
    current_track = None

    @staticmethod
    def changeMusic(music_filename):
        if music_filename is not None:
            if MusicManager.current_track != music_filename:
                MusicManager.current_track = music_filename
                pygame.mixer.music.load(music_filename)
                pygame.mixer.music.play(-1)

