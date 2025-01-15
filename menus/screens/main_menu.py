import pygame as pg
from menus.rectangles.button import Button
from menus.screens.screen_parent import BaseScreen

class MainMenu(BaseScreen):
    def __init__(self, screen, state):
        super().__init__(screen, state)

        play_button = Button(screen, 0.18, "game", text="Play", size_add=50)
        settings_button = Button(screen, 0.34, "settings", text="Settigs", size_add=50)
        player_button = Button(screen, 0.5, "character", text="Player TBD", size_add=50)
        quit_button = Button(screen, 0.66, "quit", text='Quit', size_add=50)

        self.button_list.extend([play_button, settings_button, player_button, quit_button])

