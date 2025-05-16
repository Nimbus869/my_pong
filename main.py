import pygame
from constants import *

class Main():
    pygame.init()
    display_surface = pygame.display.set_mode(size=(WINDOW_WIDTH,WINDOW_HIGHT))
    pygame.display.set_caption("My Pong")
    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                is_running = False
        display_surface.fill("blue")
        pygame.display.update()
    pygame.quit()