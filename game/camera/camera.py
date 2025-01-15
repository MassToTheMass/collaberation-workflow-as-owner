from menus.settings import settings

class Camera(): # stores all information related to the camera
    def __init__(self, world_height, world_width):
        self.screen_width = settings.getResolution()[0]
        self.screen_height = settings.getResolution()[1]
        
        self.world_width = world_height
        self.world_height = world_width

    def calculateOffset(self, player):
        self.camera_x = player.x - self.screen_width // 2 + player.width // 2
        self.camera_y = player.y - self.screen_height // 2 + player.height // 2

        self.camera_x = max(0, min(self.camera_x, self.world_width - self.screen_width))
        self.camera_y = max(0, min(self.camera_y, self.world_height - self.screen_height))