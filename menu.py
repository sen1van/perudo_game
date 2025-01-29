from pygame import Vector2, draw, surface, draw, Rect
from pygame.locals import *

from utils import draw_text, draw_text_center

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
    
    def draw_button_center(self, button_text, button_pos):
        if button_text not in self.buttons:
            self.buttons[button_text] = [self.base_size, 0]
        button_pos = (button_pos[0], button_pos[1] - self.buttons[button_text][0] + self.base_size)
        text_col = draw_text_center(self.canvas, self.font, button_text, self.buttons[button_text][0], button_pos)
        if text_col.collidepoint(self.mouse_pos):
            self.buttons[button_text][1] -= (self.buttons[button_text][0] - self.selected_size) * 2
            self.buttons[button_text][1] *= 0.3
            self.buttons[button_text][0] += int(self.buttons[button_text][1])
            self.draw_cursor = False
            if self.mouse_down == 1:
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
                
        if self.draw_button_center('Играть', (self.size.x / 2, 400)):
            events.append('start game')
        if self.draw_button_center('Выход', (self.size.x / 2, 500)):
            events.append('quit')

            
        return (self.canvas, events)