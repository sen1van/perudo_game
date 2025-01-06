from pygame import font, Vector2
from pygame.locals import *

def draw_text(surface, font_file, text, font_size, font_pos, color='black', bg_color=None):
    text = font.Font(font_file, font_size).render(text, False, color, bg_color)
    surface.blit(text, font_pos)
    return text.get_rect().move(font_pos)
    
def to_center_transiton(screen_size, canvas_size):
    if screen_size.x / screen_size.y > canvas_size.x / canvas_size.y:
        scale_f = screen_size.y / canvas_size.y
        to_center = Vector2((screen_size.x - (canvas_size.x * scale_f)) // 2, 0)
    else:
        scale_f = screen_size.x / canvas_size.x
        to_center = Vector2(0, (screen_size.y - (canvas_size.y * scale_f)) // 2)
    return {'scale': scale_f, 'move': to_center}