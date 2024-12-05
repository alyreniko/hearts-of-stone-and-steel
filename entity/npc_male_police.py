import pygame
from classes.npc import NPC
from utils.dialog import DialogWindow
import utils.variables as var


class NPCMalePolice(NPC):
    def __init__(self, x, y, width, height, path, last_image_number):
        super().__init__(x, y, width, height, path, last_image_number)
        self.dialog = DialogWindow(var.SCREEN_WIDTH, var.SCREEN_HEIGHT, "assets/texts/npc_male_police.txt")
    
    def action(self):
        self.dialog.activated = True