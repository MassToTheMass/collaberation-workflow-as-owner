import pygame as pg
from menus.rectangles.button import Button
from menus.screens.screen_parent import BaseScreen

class PlayerScreen(BaseScreen):
    def __init__(self, screen, state):
        super().__init__(screen, state)

        back_button = Button(screen, 0.05, "menu", text="Return", size_add=50)
        self.button_list.append(back_button)

    def render(self, screen, events=...):
        super().render(screen, events)
        
