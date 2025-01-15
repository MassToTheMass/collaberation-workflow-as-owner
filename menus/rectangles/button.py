import pygame as pg
from menus.rectangles.text_rect import TextRect

class Button(TextRect):
    def __init__(self, surface, y_relative, action, x_relative=0.5, color=(50, 50, 150), alt_color=(50, 50, 200), text="", size_add=1):

        super().__init__(surface, y_relative, text, x_relative, color, size_add)

        self.alt_color = alt_color
        self.size_add = size_add
        self.action = action

        # variables changed later
        self.is_selected = False



    def draw(self): # function for drawing the button

        # setting the color to if the button is selected or not
        color = self.color
        if self.is_selected:
            color = self.alt_color


        # second rectangle inside the other one, just design choice
        second_rect = pg.Rect(self.rect.x + 5, self.rect.y + 5, self.rect.width - 10, self.rect.height - 10)

        pg.draw.rect(self.surface, color, self.rect, border_radius=3)
        pg.draw.rect(self.surface, (0, 0, 0), second_rect, 5, border_radius=3)
        self.surface.blit(self.text, self.text_rect)


    def checkIfSelected(self, mouse_pos): # check if button is selected
        if self.rect.colliderect(pg.Rect(mouse_pos[0], mouse_pos[1], 1, 1)):
            self.is_selected = True
        else:
            self.is_selected = False