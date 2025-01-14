from pygame import Vector2, draw, surface, draw, Rect
from pygame.locals import *

from utils import draw_text

class Menu:
    def __init__(self, font):
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
    
    def render(self, mouse_pos,  mouse_down):
        self.mouse_pos = mouse_pos
        self.mouse_down = mouse_down
        self.cursor_vel -= (self.cursor_pos - mouse_pos) * 0.1
        self.cursor_vel *= 0.7
        self.cursor_pos += self.cursor_vel
        self.canvas.fill('white')
        self.draw_cursor = True
        
        events = []
        
        draw.circle(self.canvas, 'black', mouse_pos, 2)
        
        self.draw_button('Играть', (60, 400))
        self.draw_button('Настройки', (60, 500))
        if self.draw_button('Выход', (60, 600)):
            events.append('quit')

        if self.draw_cursor:
            self.cursor_size = min(self.cursor_size + 1, self.cursor_default)
        else:
            self.cursor_size = max(self.cursor_size ** 0.8, 0)
        draw.circle(self.canvas, 'black', self.cursor_pos, self.cursor_size, 2)
            
        return (self.canvas, events)