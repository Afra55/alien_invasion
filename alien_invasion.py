import pygame
from pygame.sprite import Group

import game_functions as gf
from game_stats import GameStatus
from settings import Settings
from ship import Ship


def run_game():

    settings = Settings()

    pygame.init()   # 初始化游戏并创建一个屏幕对象
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Afra55 game")
    stats = GameStatus(settings)

    ship = Ship(settings, screen)

    bullets = Group()

    aliens = Group()

    gf.create_fleet(settings, screen, ship, aliens)

    while True:
        gf.check_events(settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets, aliens, settings, screen, ship)
            gf.update_aliens(settings, aliens, ship, stats, screen, bullets)
            gf.update_screen(settings, screen, ship, aliens, bullets)


run_game()
