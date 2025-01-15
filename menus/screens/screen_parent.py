import pygame as pg
from menus.rectangles.button import Button
from menus.settings import settings

class BaseScreen():
    def __init__(self, screen, state):
        self.state = state

        self.button_list = []
        self.rect_list = []

    def checkButtonsSelected(self):
        for button in self.button_list:
            mouse_pos = pg.mouse.get_pos()
            button.checkIfSelected(mouse_pos)

    def handleEvent(self, event):

        if event.type == pg.MOUSEBUTTONDOWN:
            for button in self.button_list:
                if button.is_selected:
                    return button.action
        if event.type == pg.VIDEORESIZE:
            self.resize()
        return self.state
    
    def render(self, screen, events=[]):
        for button in self.button_list:
            button.draw()
        for rect in self.rect_list:
            rect.draw()

    def resize(self):
        for button in self.button_list:
            button.resizeRect()
        for rect in self.rect_list:
            rect.resizeRect()

        self.screen_w, self.screen_h = settings.getResolution()[0], settings.getResolution()[1]
