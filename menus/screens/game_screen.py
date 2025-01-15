import pygame as pg
from menus.rectangles.button import Button
from menus.screens.screen_parent import BaseScreen
from characters.player import Player
from characters.enemy import Enemy
from game.camera.camera import Camera

class GameScreen(BaseScreen):
    def __init__(self, screen, state):
        super().__init__(screen, state)

        self.player = Player(1000, 1000)
        self.enemy = Enemy(100, 3)
        self.camera = Camera(3500, 3000) # get starting dimensions of the dungeon
        self.camera.calculateOffset(self.player)

    def render(self, screen, events):
        super().render(screen, events)

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.player.y -= self.player.speed
        if keys[pg.K_s]:
            self.player.y += self.player.speed
        if keys[pg.K_a]:
            self.player.x -= self.player.speed
        if keys[pg.K_d]:
            self.player.x += self.player.speed



        image = pg.image.load("game/weapons/images/water_blast.png")



        self.camera.calculateOffset(self.player)

        # filling the background
        screen.fill((0, 0, 0))

        # just drawing a simple map
        for x in range(0, self.camera.world_width, 100):
            for y in range(0, self.camera.world_height, 100):
                pg.draw.rect(screen, (255, 255, 255), pg.Rect(x - self.camera.camera_x, y - self.camera.camera_y, 100, 100), 1)

        


        self.player.draw(screen, self.camera.camera_x, self.camera.camera_y)
        self.enemy.draw(screen, self.camera.camera_x, self.camera.camera_y)


        screen.blit(image, (1400, 255))

    