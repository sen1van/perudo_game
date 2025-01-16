import pygame
import random
from pygame.locals import *
from PIL import Image


def line(string, font_size, color, pos, style=None):
    font = pygame.font.Font(style, font_size)
    text = font.render(string, 1, color)
    screen.blit(text, pos)

def len_line(string, font_size, style=None, color=(0, 0, 0)):
    font = pygame.font.Font(style, font_size)
    text = font.render(string, 1, color)
    text_width = text.get_width()
    return text_width

def image(path, size, pos):
    img = Image.open(path)
    img.thumbnail((size, size))
    blit_pil_img(screen, img, pos)

def blit_pil_img(screen, img, position):
    pygame_image = pygame.image.fromstring(img.tobytes(), img.size, "RGB")
    screen.blit(pygame_image, position)

def roll_dice(num):
    a = []
    for i in range(num):
        a.append(random.randint(1, 6))
    return a



def first_step(num):
    return random.randint(0, num - 1)


pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)



pygame.display.flip()

ACTIONS = ["Не верю", "Ровно"]
run = True
players_dice = {}
num_player_dice = {}
bet = {}
user_name = "Player"
names = ["Bot_Vasya", "Bot_Oleg", "Bot_Petya", "Bot_Anna", "Bot_Nastya"]

for name in names:
    num_player_dice[name] = 6
    players_dice[name] = roll_dice(6)
players_dice[user_name] = roll_dice(6)





black = (0, 0, 0)
blue = (0, 162, 232)
step = first_step(6)
num_dice = 1
max_num_dice = 36
val_dice = 1
max_val_dice = 6
step = 5
button_is_pressed = False
input_field_visability = False

while run:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pos[0] >= 1540 and pos[0] <= 1880 and pos[1] >= 990 and pos[1] <= 1025 and event.button == 1:
                button_is_pressed = True
            if input_field_visability:
                if pos[0] >= 790 and pos[0] <= 1110 and pos[1] >= 817 and pos[1] <= 842 and event.button == 1:
                    button_is_pressed = True

                if pos[0] >= 790 and pos[0] <= 1110 and pos[1] >= 787 and pos[1] <= 812 and event.button == 1:
                    button_is_pressed = True
                
                if pos[0] >= 950 and pos[0] <= 1010 and pos[1] >= 717 and pos[1] <= 777:
                    if event.button == 4:
                        val_dice += 1
                        if val_dice > max_val_dice:
                            val_dice = 1
                    if event.button == 5:
                        val_dice -= 1
                        if val_dice < 1:
                            val_dice = 6

                if pos[0] >= 880 and pos[0] <= 940 and pos[1] >= 717 and pos[1] <= 777:
                    if event.button == 4:
                        num_dice += 1
                        if num_dice > max_num_dice:
                            num_dice = 1
                    if event.button == 5:
                        num_dice -= 1
                        if num_dice < 1:
                            num_dice = max_num_dice

    screen.fill((255, 255, 255))
    #area
    pygame.draw.rect(screen, (200, 200, 200), (110, 100, 1700, 920), 3, 15)
    #user area
    pygame.draw.rect(screen, (255, 255, 255), (35, 860, 385, 185), 0, 15)
    pygame.draw.rect(screen, (255, 255, 255), (35, 875, 370, 170), 0, 15)
    pygame.draw.rect(screen, (0, 0, 0), (35, 875, 370, 170), 3, 15)
    #button area
    pygame.draw.rect(screen, (255, 255, 255), (1510, 860, 385, 185), 0, 15)
    pygame.draw.rect(screen, (255, 255, 255), (1525, 875, 370, 170), 0, 15)
    pygame.draw.rect(screen, (0, 0, 0), (1525, 875, 370, 170), 3, 15) 
    #title
    # line("Perudo", 52, (200, 200, 200), (850, 500), style="fonts/unicephalon.otf")
    #user avatar
    image("perudo_images/users/anon_user.jpg", 140, (50, 890))
    #user name
    if step != 5:
        line(user_name, 30, black, (220, 890))
        line("Ход оппонента", 45, (0, 0, 0), (1600, 950))
        
    else:
        if pos[0] >= 1540 and pos[0] <= 1880 and pos[1] >= 895 and pos[1] <= 930:
            pygame.draw.rect(screen, (0, 0, 0), (1540, 895, 340, 35), 3, 8)
        else:
            pygame.draw.rect(screen, (200, 200, 200), (1540, 895, 340, 35), 3, 8) 
        line("Не верю!", 30, (0, 0, 0), (1670, 905))
        if pos[0] >= 1540 and pos[0] <= 1880 and pos[1] >= 945 and pos[1] <= 980:
            pygame.draw.rect(screen, (0, 0, 0), (1540, 945, 340, 35), 3, 8)
        else:
            pygame.draw.rect(screen, (200, 200, 200), (1540, 945, 340, 35), 3, 8)
        line("Ровно!", 30, (0, 0, 0), (1685, 955))
        if pos[0] >= 1540 and pos[0] <= 1880 and pos[1] >= 990 and pos[1] <= 1025:
            pygame.draw.rect(screen, (0, 0, 0), (1540, 990, 340, 35), 3, 8)
            if button_is_pressed:
                input_field_visability = True
                button_is_pressed = False
        else:
            pygame.draw.rect(screen, (200, 200, 200), (1540, 990, 340, 35), 3, 8)
        line("Поднять ставку", 30, (0, 0, 0), (1640, 1000))
        line(user_name, 30, blue, (220, 890))
        if input_field_visability:
            line("Наведитесь на поле и крутите", 28, (0, 0, 0), (805, 670))
            line("колесико мыши", 28, (0, 0, 0), (870, 690))
            pygame.draw.rect(screen, (0, 0, 0), (780, 660, 340, 190), 3, 8)
            pygame.draw.rect(screen, (0, 0, 0), (880, 717, 60, 60), 2, 4)
            line(str(num_dice), 50, (0, 0, 0), (901 - (10 * (len(str(num_dice)) - 1)), 731))
            image(f"perudo_images/dice/dice{val_dice}.jpg", 60, (950, 717))
            line("Подтвердить", 28, (0, 0, 0), (880, 790))
            pygame.draw.rect(screen, (200, 200, 200), (790, 787, 320, 25), 2, 4)
            if pos[0] >= 790 and pos[0] <= 1110 and pos[1] >= 787 and pos[1] <= 812:
                pygame.draw.rect(screen, (0, 0, 0), (790, 787, 320, 25), 2, 4)
                if button_is_pressed:
                    print("qwezxc")
                    input_field_visability = False
                    button_is_pressed = False
                    bet["val"] = val_dice
                    bet["num"] = num_dice
                    val_dice = 1
                    num_dice = 1
                    step = 0
            line("Отмена", 28, (0, 0, 0), (910, 820))
            pygame.draw.rect(screen, (200, 200, 200), (790, 817, 320, 25), 2, 4)
            if pos[0] >= 790 and pos[0] <= 1110 and pos[1] >= 817 and pos[1] <= 842:
                pygame.draw.rect(screen, (0, 0, 0), (790, 817, 320, 25), 2, 4)
                if button_is_pressed:
                    input_field_visability = False
                    button_is_pressed = False
                    val_dice = 1
                    num_dice = 1
    #rating
    line("Рейтинг: 9678", 30, (0, 0, 0), (220, 920))
    #menu
    # image("perudo_images\icons\menu.jpg", 50, (220, 980))
    image("perudo_images\icons\menu.jpg", 50, (1830, 30))
    #area for dice
    #pygame.draw.rect(screen, (34, 34, 34), (535, 880, 800, 150), 3, 15)
    #dice
    for i in range(1, 7):
        image(f"perudo_images/dice/dice{players_dice[user_name][i - 1]}.jpg", 120, (550 + (i - 1) * 130, 880))

    #enemy
    color = black
    for i in range(1, 4):
        if i == step:
            color = blue
        pos_img_x = 475 + (i - 1) * 425
        pygame.draw.rect(screen, (255, 255, 255), (pos_img_x - 15, 25, 150, 170), 0, 15)
        image("perudo_images/users/bot.jpg", 120, (pos_img_x, 40))
        len_name = len_line(names[i], 24)
        pos_line_x = 475 + (i - 1) * 425 + 60 - len_name//2
        line(names[i], 24, color, (pos_line_x, 170), style=None)
        line(f"{players_dice[names[i]]}", 24, color, (pos_line_x, 190), style=None)
        color = black

    for i in (0, 4):
        if i == step:
            color = blue
        if i == 0:
            pygame.draw.rect(screen, (255, 255, 255), (35, 415, 150, 175), 0, 15)
            image("perudo_images/users/bot.jpg", 120, (50, 430))
        else:
            pygame.draw.rect(screen, (255, 255, 255), (1700, 415, 150, 175), 0, 15)
            image("perudo_images/users/bot.jpg", 120, (1750, 430))
        len_name = len_line(names[i], 24)
        pos_line_x = 475 + (i - 1) * 425 + 60 - len_name//2
        line(names[i], 24, color, (pos_line_x, 560))
        line(f"{players_dice[names[i]]}", 24, color, (pos_line_x, 580), style=None)
        color = black

    #info string
    # len_name = len_line("Ставка: 5", 60)
    # pos_line_x =  960 - len_name // 2 - 65
    # line("Ставка: 5", 60, (0, 0, 0), (pos_line_x, 485))
    # image("perudo_images/dice/dice6.jpg", 50, (905 + len_name // 2, 477))
    if len(bet) != 0:
        line(f"Ставка: {bet["num"]}", 60, (0, 0, 0), (800, 485))
        image(f"perudo_images/dice/dice{bet["val"]}.jpg", 50, (1000 + (25 * (len(str(bet["num"])) - 1)), 477))
    
    

    pygame.display.update()


pygame.quit()
