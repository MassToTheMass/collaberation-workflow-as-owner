import pygame as pg
from menus.rectangles.button import Button
from menus.screens.screen_parent import BaseScreen
from menus.rectangles.rect_draw import DrawRect
from menus.rectangles.text_rect import TextRect
from menus.settings import settings
from menus.rectangles.slider import MySlider
import pygame_widgets as pgw

class SettingsScreen(BaseScreen):
    def __init__(self, screen, state):
        super().__init__(screen, state)

        self.slider_list = []

        back_button = Button(screen, 0.05, "menu", text="Return", size_add=50)
        self.button_list.append(back_button)


        # create rectangles for the settings menu
        outline_rect = DrawRect(screen, 0.15, 0.8, 1, color=(50, 50, 100))
        self.rect_list.append(outline_rect)

        # creating a slider for different settings
        self.fps_rect = TextRect(screen, 0.29, f"FPS: {settings.getFPS()}", 0.28, size_add=50)
        self.fps_slider = MySlider(screen, 0.42, 0.28, 0.4, 0.1, min=15, max=120, initial=settings.getFPS())

        self.rect_list.append(self.fps_rect)
        self.slider_list.append(self.fps_slider)

    def resize(self):
        super().resize()
        for slider in self.slider_list:
            slider.resize()

    def render(self, screen, events):
        super().render(screen)
        pgw.update(events)
        self._updateLabels()

    def _updateLabels(self):
        
        self.fps_rect.updateText(f"FPS: {self.fps_slider.value}")
        settings.setFPS(self.fps_slider.value)