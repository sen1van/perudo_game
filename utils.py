from pygame import font, Vector2
import pygame
from PIL import Image
from pygame.locals import *


fonts = dict()

def draw_text(surface, font_file, text, font_size, font_pos, color='black', bg_color=None):
    if font_size not in fonts:
        fonts[font_file + str(font_size)] = font.Font(font_file, font_size)
    text = fonts[font_file + str(font_size)].render(text, False, color, bg_color)
    surface.blit(text, font_pos)
    return text.get_rect().move(font_pos)

def draw_text_center(surface, font_file, text, font_size, font_pos, color='black', bg_color=None):
    if font_size not in fonts:
        fonts[font_file + str(font_size)] = font.Font(font_file, font_size)
    text = fonts[font_file + str(font_size)].render(text, False, color, bg_color)
    font_pos = Vector2(*font_pos)
    surface.blit(text, font_pos - Vector2(text.get_size()[0] / 2, 0))
    return text.get_rect().move(font_pos - Vector2(text.get_size()[0] / 2, 0))
    
images = dict()

def draw_image(surface, path, pos, size):
    if path not in images:
        images[path] = Image.open(path)
    img = images[path]
    img.thumbnail((size, size))
    pygame_image = pygame.image.fromstring(img.tobytes(), img.size, "RGB")
    surface.blit(pygame_image, pos)


def to_center_transiton(screen_size, canvas_size):
    if screen_size.x / screen_size.y > canvas_size.x / canvas_size.y:
        scale_f = screen_size.y / canvas_size.y
        to_center = Vector2((screen_size.x - (canvas_size.x * scale_f)) // 2, 0)
    else:
        scale_f = screen_size.x / canvas_size.x
        to_center = Vector2(0, (screen_size.y - (canvas_size.y * scale_f)) // 2)
    return {'scale': scale_f, 'move': to_center}