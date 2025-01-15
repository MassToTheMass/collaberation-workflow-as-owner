import pygame as pg

class Player():
    def __init__(self, x=200, y=200):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.speed = 6

    def draw(self, screen, camera_x, camera_y):
        pg.draw.rect(screen, "Blue", pg.Rect(self.x - camera_x, self.y - camera_y, self.width, self.height), border_radius=5)
    