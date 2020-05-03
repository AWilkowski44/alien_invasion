import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #Inicjalizacja Pygame, ustawień i obiektu ekranu.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Inwazja obcych")
    
    #Utworzenie statku kosmicznego, grupy pocisków, grupy obcych.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    #Utworzenie floty obcych.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    #Rozpoczęcie pętli głównej gry.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
                

    
run_game()
  
