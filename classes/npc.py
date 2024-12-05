import pygame
import utils.variables as var
from classes.interaction import Interaction
from utils.control import Control


class NPC():
    def __init__(self, x, y, width, height, path, last_image_number):
        """
        Инициализация объекта NPC.

        :param x: int, x позиция NPC
        :param y: int, y позиция NPC
        :param width: int, ширина NPC
        :param height: int, высота NPC
        :param path: str, путь к папке с изображениями NPC
        :param last_image_number: int, номер последнего изображения в папке
        """
        self.path = path
        self.width, self.height = width, height
        self.images = [
            pygame.transform.scale(
                pygame.image.load(f"{self.path}/{i}.png").convert_alpha(), (width, height)
            ) for i in range(1, last_image_number)
        ]
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.font = pygame.font.Font("assets/fonts/Catacombs.ttf", 80)
        self.text = self.font.render('E', True, (0, 0, 255))
        self.frame_count = 0

    def update(self, player_rect, camera):
        """
        Обновляет анимацию NPC и проверяет взаимодействие с игроком.

        Этот метод обновляет текущее изображение NPC для анимации, проверяет 
        столкновение с прямоугольником игрока и обрабатывает взаимодействие, 
        если игрок находится в пределах досягаемости. Если происходит 
        взаимодействие, отображает текст взаимодействия и выполняет действие 
        NPC, если нажата клавиша взаимодействия. Кроме того, обновляет окно 
        диалога NPC.

        :param player: Прямоугольник игрока, используемый для обнаружения столкновений.
        :param camera: Объект камеры, используемый для вычисления позиции NPC на экране.
        """
        if self.frame_count % 4 == 0:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]
        
        self.frame_count += 1

        interaction_rect = camera.apply(self.rect)
        var.SCREEN.blit(self.image, interaction_rect)

        collide = self.rect.collidepoint(player_rect.centerx, player_rect.centery)
        if collide:
            text_pos = (
                interaction_rect.center[0] - (self.text.get_width() // 2),
                interaction_rect.center[1] - self.image.get_height() - 50
            )
            var.SCREEN.blit(self.text, text_pos)
            if Control.check_press(var.INTERACT):
                self.action()
        