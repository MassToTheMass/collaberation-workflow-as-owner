from pygame_widgets.slider import Slider
import pygame_widgets
import pygame as pg

class MySlider(Slider):
    def __init__(self, win, x_rel, y_rel, rel_width, rel_height, **kwargs):
        x = int(round(x_rel * win.get_width()))
        y = int(round(y_rel * win.get_height()))
        width = int(round(rel_width * win.get_width()))
        height = int(round(rel_height * win.get_height()))
        super().__init__(win, x, y, width, height, **kwargs)

        self.win = win
        self.x_rel = x_rel
        self.y_rel = y_rel
        self.rel_width = rel_width
        self.rel_height = rel_height



    def resize(self):

        self.x = int(round(self.x_rel * self.win.get_width()))
        self.y = int(round(self.y_rel * self.win.get_height()))
        self._width = int(round(self.rel_width * self.win.get_width()))
        self._height = int(round(self.rel_height * self.win.get_height()))

        self.handleRadius = int(self._height / 2)

        # set internal representation of slider
        self.setX(self.x)
        self.setY(self.y)
        self.setWidth(self._width)
        self.setHeight(self._height)
    
    def draw(self):
        # Ensure the handle radius is scaled when drawing the slider
        pg.draw.rect(self.win, self.colour, (self.getX(), self.getY(), self.getWidth(), self.getHeight()), border_radius=self.handleRadius)
        
        # Calculate the handle's X position, adjusting by the handle's radius to center it properly
        handleX = self.getX() + int((self.value - self.min) / (self.max - self.min) * self.getWidth())
        
        # Draw the handle as a circle with the updated radius
        pg.draw.circle(self.win, self.handleColour, (handleX, self.getY() + self.getHeight() // 2), self.handleRadius * 1.5)
