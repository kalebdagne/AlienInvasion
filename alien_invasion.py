import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions
from pygame.sprite import Group
from alien import Alien

def run_game():

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")


    # Make a ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()
    aliens = Group()
    game_functions.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        game_functions.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        game_functions.update_bullets(ai_settings, screen, ship, aliens, bullets)
        game_functions.update_aliens(ai_settings, ship, aliens)
        game_functions.update_screen(ai_settings, screen, ship, aliens, bullets)



run_game()


