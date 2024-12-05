import pygame
import utils.variables as var
from utils.control import Control


class DialogWindow:
    def __init__(self, width, height, text_file, separator="---"):
        self.width = width
        self.height = height // 3
        self.font = pygame.font.Font(None, 36)
        self.texts = []
        with open(text_file, "r") as file:
            block = ""
            for line in file:
                if line.strip() == separator:
                    self.texts.append(block.strip())
                    block = ""
                else:
                    block += line
            self.texts.append(block.strip())
        self.current_text_index = 0
        self.text_surface = self.render_text(self.texts[self.current_text_index])
        self.dialog_rect = pygame.Rect(0, height - self.height, self.width, self.height)
        self.continue_text = self.font.render("Нажмите ПРОБЕЛ чтобы продолжить...", True, (255, 255, 255))
        self.activated = False

    def render_text(self, text):
        lines = text.split("\n")
        rendered_lines = [self.font.render(line, True, (255, 255, 255)) for line in lines]
        return rendered_lines

    def update(self):
        if self.activated:
            print(self.current_text_index)
            pygame.draw.rect(var.SCREEN, (0, 0, 0), self.dialog_rect)
            for i, line_surface in enumerate(self.text_surface):
                var.SCREEN.blit(line_surface, (20, self.dialog_rect.y + 30 + i * (self.font.get_height() + 5)))
            var.SCREEN.blit(self.continue_text, (self.width - self.continue_text.get_width() - 20, self.dialog_rect.y + self.height - self.continue_text.get_height() - 10))

            for event in Control.events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.current_text_index += 1
                        if self.current_text_index >= len(self.texts):
                            self.activated = False
                            self.current_text_index = 0
                            self.text_surface = self.render_text(self.texts[self.current_text_index])
                        else:
                            self.text_surface = self.render_text(self.texts[self.current_text_index])
