import pygame

import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():

    settings = Settings()

    pygame.init()   # 初始化游戏并创建一个屏幕对象
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Afra55 game")

    ship = Ship(settings, screen)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(settings, screen, ship)


run_game()
