import pygame
from pygame.locals import *

from menu import Menu
from perudo_new import Perudo
from end_menu import EndMenu
from utils import to_center_transiton, add_log

pygame.init()
screen = pygame.display.set_mode((1200, 800), RESIZABLE)
clock = pygame.time.Clock()
running = True

pygame.display.set_caption('PIPPOG')
# pygame.mouse.set_visible(False)

game = Menu('Comial4448.ttf')
mouse_event = -1

while running:
    mouse_event = -1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_event = event.button
    
    screen.fill('black')

    to_center = to_center_transiton(pygame.Vector2(*screen.get_size()), game.size)
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    mouse_pos -= to_center['move']
    mouse_pos /= to_center['scale']
    
    game_surface, actions = game.render(mouse_pos, mouse_event)
    game_surface = pygame.transform.scale_by(game_surface, to_center['scale'])
    
    if 'quit' in actions:
        running = False
        add_log('quiting...')
    
    if 'start game' in actions:
        game = Perudo('Comial4448.ttf')
        add_log('game start')
        
    if 'game over' in actions:
        game = EndMenu('Comial4448.ttf', actions[-1])
        add_log('game over')
    
    if 'exit' in actions:
        game = Menu('Comial4448.ttf')
        add_log('player exit')
    
    
    screen.blit(game_surface, to_center['move'])
    pygame.display.flip()
    # print(mouse_event)
    clock.tick(60)

pygame.quit()