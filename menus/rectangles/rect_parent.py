import pygame as pg

class BaseRect():
    def __init__(self, surface, y_relative, x_relative=0.5, color=(50, 50, 150)):
        self.y_rel = y_relative
        self.x_rel = x_relative
        self.color = color
        self.surface = surface

        self.rect = pg.Rect(self.x_rel * self.surface.get_width(), self.y_rel * self.surface.get_height(), 25, 25) # chagne the 25s in other classes but at least we can see in case no redefinition


    def draw(self): # function for drawing the rect

        color = self.color
        # second rectangle inside the other one, just design choice
        second_rect = pg.Rect(self.rect.x + 5, self.rect.y + 5, self.rect.width - 10, self.rect.height - 10)

        pg.draw.rect(self.surface, color, self.rect, border_radius=3)
        pg.draw.rect(self.surface, (0, 0, 0), second_rect, 5, border_radius=3)