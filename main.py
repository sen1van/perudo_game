import pygame
from pygame.locals import *

from menu import Menu
from utils import to_center_transiton

pygame.init()
screen = pygame.display.set_mode((1280, 853), RESIZABLE)
clock = pygame.time.Clock()
running = True

pygame.display.set_caption('PIPPOG')
pygame.mouse.set_visible(False)

menu = Menu('NotoSerifDisplay.ttf')
mouse_down = False

while running:
    mouse_down = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
    
    screen.fill('black')

    to_center = to_center_transiton(pygame.Vector2(*screen.get_size()), menu.size)
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    mouse_pos -= to_center['move']
    mouse_pos /= to_center['scale']
    
    menu_surface, actions = menu.render(mouse_pos, mouse_down)
    menu_surface = pygame.transform.scale_by(menu_surface, to_center['scale'])
    
    if 'quit' in actions:
        running = False
    
    screen.blit(menu_surface, to_center['move'])
    pygame.display.flip()
    clock.tick(60)

pygame.quit()