import pygame as pg
from menus.rectangles.rect_parent import BaseRect

class DrawRect(BaseRect):
    def __init__(self, surface, y_relative, width_rel, height_rel, x_relative=0.5, color=(50, 50, 150)):
        super().__init__(surface, y_relative, x_relative, color)
        self.rect = pg.Rect(0, self.y_rel * surface.get_height(), width_rel * surface.get_width(), height_rel * surface.get_height())
        self.rect.centerx = self.x_rel * surface.get_width()
        self.width_rel = width_rel
        self.height_rel = height_rel

    def resizeRect(self):

        self.rect.y = self.y_rel * self.surface.get_height()
        self.rect.width = self.width_rel * self.surface.get_width()
        self.rect.height = self.height_rel * self.surface.get_height()
        self.rect.centerx = self.x_rel * self.surface.get_width()

        