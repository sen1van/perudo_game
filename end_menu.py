from pygame import Vector2, draw, surface, draw, Rect
from pygame.locals import *

from utils import draw_text, draw_text_center

class EndMenu:
    def __init__(self, font, who_win):
        self.winner = who_win
        self.size = Vector2(1200, 800)
        
        self.cursor_pos = Vector2()
        self.cursor_vel = Vector2()
        self.draw_cursor = True
        
        self.cursor_size = 15
        self.cursor_default= 15
        
        self.mouse_pos = Vector2()
        self.mouse_down = False
        
        self.font = font
        
        self.buttons = dict()
        self.base_size = 60
        self.selected_size = 80
        
        
        self.canvas = surface.Surface(self.size, SRCALPHA)
        
    def draw_button(self, button_text, button_pos):
        if button_text not in self.buttons:
            self.buttons[button_text] = [self.base_size, 0]
        button_pos = (button_pos[0], button_pos[1] - self.buttons[button_text][0] + self.base_size)
        text_col = draw_text(self.canvas, self.font, button_text, self.buttons[button_text][0], button_pos)
        if text_col.collidepoint(self.mouse_pos):
            self.buttons[button_text][1] -= (self.buttons[button_text][0] - self.selected_size) * 0.5
            self.buttons[button_text][1] *= 0.3
            self.buttons[button_text][0] += int(self.buttons[button_text][1])
            self.draw_cursor = False
            if self.mouse_down:
                return True
        else:
            self.buttons[button_text][1] -= (self.buttons[button_text][0] - self.base_size) * 0.5
            self.buttons[button_text][1] *= 0.3
            self.buttons[button_text][0] += int(self.buttons[button_text][1])
        return False
    
    def render(self, mouse_pos,  mouse_event):
        self.mouse_pos = mouse_pos
        self.mouse_down = mouse_event == 1
        self.canvas.fill('white')
        self.draw_cursor = True
        
        events = []
        draw_text_center(self.canvas, self.font, 'ИГРА ОКОНЧЕНА', 50, (self.size.x / 2, self.size.y / 4))
        draw_text_center(self.canvas, self.font, self.winner, 50, (self.size.x / 2, self.size.y / 4 * 2))
        if self.draw_button('Ещё раз', (60, 400)):
            events.append('start game')
        if self.draw_button('Выход', (60, 500)):
            events.append('quit')

            
        return (self.canvas, events)