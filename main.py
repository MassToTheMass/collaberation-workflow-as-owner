import pygame as pg
import sys
from menus.settings import settings
from menus.rectangles.button import Button
from menus.screens.main_menu import MainMenu
from menus.screens.game_screen import GameScreen
from menus.screens.settings_screen import SettingsScreen
from menus.screens.player_screen import PlayerScreen
from game.camera.camera import Camera

pg.init()

# definig some strings so that we can see which class to display
STATE_MENU = 'menu'
STATE_GAME = "game"
STATE_SETTINGS = "settings"
STATE_QUIT = "quit"
STATE_PLAYER = "character"

def main():

    # initializing saved settings preset
    fps = settings.getFPS()
    screen_width, screen_height = settings.getResolution()[0], settings.getResolution()[1]

    # initializig pygame variables for the screen
    done = False
    screen = pg.display.set_mode((screen_width, screen_height), flags=pg.RESIZABLE)
    clock = pg.time.Clock()

    #initializing all different screens/game loops
    current_state = STATE_MENU
    previous_state = STATE_MENU
    menu_screen = MainMenu(screen, STATE_MENU)
    settings_screen = SettingsScreen(screen, STATE_SETTINGS)
    game_screen = GameScreen(screen, STATE_GAME)
    player_screen = PlayerScreen(screen, STATE_PLAYER)

    states_dictionary = {
        STATE_MENU : menu_screen,
        STATE_GAME : game_screen,
        STATE_SETTINGS : settings_screen,
        STATE_PLAYER : player_screen,
    }


    while not done:

        if previous_state != current_state:
            states_dictionary[current_state].resize()
            if previous_state == STATE_SETTINGS: # update all settings here
                fps = settings.getFPS()
            previous_state = current_state

        states_dictionary[current_state].checkButtonsSelected()

        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT or current_state == STATE_QUIT:
                pg.quit()
                sys.exit()
            current_state = states_dictionary[current_state].handleEvent(event)
            if current_state == STATE_QUIT:
                pg.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        states_dictionary[current_state].render(screen, events)
        
        pg.display.flip()
        clock.tick(fps)

main()