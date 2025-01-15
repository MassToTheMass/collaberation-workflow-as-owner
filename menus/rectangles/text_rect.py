from menus.rectangles.rect_parent import BaseRect
import pygame as pg

class TextRect(BaseRect):
    def __init__(self, surface, y_relative, text, x_relative=0.5, color=(50, 50, 150), size_add=1):
        super().__init__(surface, y_relative, x_relative, color)

        self.size_add = size_add


        # creating a font object for te text
        self.font = pg.font.SysFont('freesanbold.ttf', 100)
        self.text = self.font.render(text, True, (0, 0, 0))

        self.resizeRect()

    def draw(self):
        super().draw()
        self.surface.blit(self.text, self.text_rect)



    def resizeRect(self):

        self.rect = self.text.get_rect()
        self.rect.y = (self.y_rel * self.surface.get_height())
        self.rect.centerx = (self.x_rel * self.surface.get_width())
        self.text_rect = self.rect # so that the text centers into the smaller rectangle
        self.rect = self.rect.inflate(self.size_add, self.size_add) # increase the rectangle size so there is "padding" on the sides of the text

    def updateText(self, text):

        self.font = pg.font.SysFont('freesanbold.ttf', 100)
        self.text = self.font.render(text, True, (0, 0, 0))
        self.resizeRect()
