import pygame as pg

class Enemy():
    def __init__(self, health, size):
        self.health = health
        self.size = size

    def draw(self, screen, camera_x, camera_y):
        pg.draw.rect(screen, (150, 50, 50), pg.Rect(1500 - camera_x, 400 - camera_y, 50, 50), border_radius=5)