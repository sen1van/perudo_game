import pygame
import random
from pygame.locals import *
from PIL import Image


pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

class Output:
    def line(self, string, font_size, color, pos, style=None):
        self.font = pygame.font.Font(style, font_size)
        self.text = self.font.render(string, 1, color)
        screen.blit(self.text, pos)

    def len_line(self, string, font_size, style=None, color=(0, 0, 0)):
        self.font = pygame.font.Font(style, font_size)
        self.text = self.font.render(string, 1, color)
        self.text_width = self.text.get_width()
        return self.text_width

    def image(self, path, size, pos):
        self.img = Image.open(path)
        self.img.thumbnail((size, size))
        self.blit_pil_img(screen, self.img, pos)

    def blit_pil_img(self, screen, img, position):
        self.pygame_image = pygame.image.fromstring(img.tobytes(), img.size, "RGB")
        screen.blit(self.pygame_image, position)

class GameFunc:
    def roll_dice(self, num):
        self.a = []
        for i in range(num):
            self.a.append(random.randint(1, 6))
        return self.a

    def first_step(self, num):
        return random.randint(0, num - 1)

class Perudo(GameFunc, Output):
    def __init__(self, user_name):
        self.ACTIONS = ["Не верю", "Ровно"]
        self.players_dice = {}
        self.num_player_dice = {}
        self.bet = {}
        self.user_name = user_name
        self.names = ["Bot_Vasya", "Bot_Oleg", "Bot_Petya", "Bot_Anna", "Bot_Nastya"]

        for name in self.names:
            self.num_player_dice[name] = 6
            self.players_dice[name] = self.roll_dice(6)
        self.players_dice[user_name] = self.roll_dice(6)

        self.black = (0, 0, 0)
        self.blue = (0, 162, 232)
        self.white = (255, 255, 255)
        self.grey = (200, 200, 200)

        self.step = self.first_step(6)
        self.num_dice = 1
        self.max_num_dice = 36
        self.val_dice = 1
        self.max_val_dice = 6
        self.button_is_pressed = False
        self.input_field_visability = False

        self.step = 5

        self.run = True

        while self.run:
            pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pos[0] >= 1540 and pos[0] <= 1880 and pos[1] >= 990 and pos[1] <= 1025 and event.button == 1:
                        self.button_is_pressed = True
                    if self.input_field_visability:
                        if pos[0] >= 790 and pos[0] <= 1110 and pos[1] >= 817 and pos[1] <= 842 and event.button == 1:
                            self.button_is_pressed = True
                        if pos[0] >= 790 and pos[0] <= 1110 and pos[1] >= 787 and pos[1] <= 812 and event.button == 1:
                            self.button_is_pressed = True
                        if pos[0] >= 950 and pos[0] <= 1010 and pos[1] >= 717 and pos[1] <= 777:
                            if event.button == 4:
                                self.val_dice += 1
                                if self.val_dice > self.max_val_dice:
                                    self.val_dice = 1
                            if event.button == 5:
                                self.val_dice -= 1
                                if self.val_dice < 1:
                                    self.val_dice = 6

                        if pos[0] >= 880 and pos[0] <= 940 and pos[1] >= 717 and pos[1] <= 777:
                            if event.button == 4:
                                self.num_dice += 1
                                if self.num_dice > self.max_num_dice:
                                    self.num_dice = 1
                            if event.button == 5:
                                self.num_dice -= 1
                                if self.num_dice < 1:
                                    self.num_dice = self.max_num_dice
            
            screen.fill(self.white)
            #area
            pygame.draw.rect(screen, self.grey, (110, 100, 1700, 920), 3, 15)
            #user area
            pygame.draw.rect(screen, self.white, (35, 860, 385, 185), 0, 15)
            pygame.draw.rect(screen, self.white, (35, 875, 370, 170), 0, 15)
            pygame.draw.rect(screen, self.black, (35, 875, 370, 170), 3, 15)
            #button area
            pygame.draw.rect(screen, self.white, (1510, 860, 385, 185), 0, 15)
            pygame.draw.rect(screen, self.white, (1525, 875, 370, 170), 0, 15)
            pygame.draw.rect(screen, self.black, (1525, 875, 370, 170), 3, 15) 
            #user avatar
            self.image("perudo_images/users/anon_user.jpg", 140, (50, 890))
            #user name
            if self.step != 5:
                self.line(user_name, 30, self.black, (220, 890))
                self.line("Ход оппонента", 45, self.black, (1600, 950))
                
            else:
                if pos[0] >= 1540 and pos[0] <= 1880 and pos[1] >= 895 and pos[1] <= 930:
                    pygame.draw.rect(screen, self.black, (1540, 895, 340, 35), 3, 8)
                else:
                    pygame.draw.rect(screen, self.grey, (1540, 895, 340, 35), 3, 8) 
                self.line("Не верю!", 30, self.black, (1670, 905))
                if pos[0] >= 1540 and pos[0] <= 1880 and pos[1] >= 945 and pos[1] <= 980:
                    pygame.draw.rect(screen, self.black, (1540, 945, 340, 35), 3, 8)
                else:
                    pygame.draw.rect(screen, self.grey, (1540, 945, 340, 35), 3, 8)
                self.line("Ровно!", 30, self.black, (1685, 955))
                if pos[0] >= 1540 and pos[0] <= 1880 and pos[1] >= 990 and pos[1] <= 1025:
                    pygame.draw.rect(screen, self.black, (1540, 990, 340, 35), 3, 8)
                    if self.button_is_pressed:
                        self.input_field_visability = True
                        self.button_is_pressed = False
                else:
                    pygame.draw.rect(screen, self.grey, (1540, 990, 340, 35), 3, 8)
                self.line("Поднять ставку", 30, self.black, (1640, 1000))
                self.line(user_name, 30, self.blue, (220, 890))
                if self.input_field_visability:
                    self.line("Наведитесь на поле и крутите", 28, self.black, (805, 670))
                    self.line("колесико мыши", 28, self.black, (870, 690))
                    pygame.draw.rect(screen, self.black, (780, 660, 340, 190), 3, 8)
                    pygame.draw.rect(screen, self.black, (880, 717, 60, 60), 2, 4)
                    self.line(str(self.num_dice), 50, self.black, (901 - (10 * (len(str(self.num_dice)) - 1)), 731))
                    self.image(f"perudo_images/dice/dice{self.val_dice}.jpg", 60, (950, 717))
                    self.line("Подтвердить", 28, self.black, (880, 790))
                    pygame.draw.rect(screen, self.grey, (790, 787, 320, 25), 2, 4)
                    if pos[0] >= 790 and pos[0] <= 1110 and pos[1] >= 787 and pos[1] <= 812:
                        pygame.draw.rect(screen, self.black, (790, 787, 320, 25), 2, 4)
                        if self.button_is_pressed:
                            self.input_field_visability = False
                            self.button_is_pressed = False
                            self.bet["val"] = self.val_dice
                            self.bet["num"] = self.num_dice
                            self.val_dice = 1
                            self.num_dice = 1
                            self.step = 0
                    self.line("Отмена", 28, self.black, (910, 820))
                    pygame.draw.rect(screen, self.grey, (790, 817, 320, 25), 2, 4)
                    if pos[0] >= 790 and pos[0] <= 1110 and pos[1] >= 817 and pos[1] <= 842:
                        pygame.draw.rect(screen, self.black, (790, 817, 320, 25), 2, 4)
                        if self.button_is_pressed:
                            self.input_field_visability = False
                            self.button_is_pressed = False
                            self.val_dice = 1
                            self.num_dice = 1
            #rating
            self.line("Рейтинг: 9678", 30, self.black, (220, 920))
            #menu
            self.image("perudo_images\icons\menu.jpg", 50, (1830, 30))
            #dice
            for i in range(1, 7):
                self.image(f"perudo_images/dice/dice{self.players_dice[self.user_name][i - 1]}.jpg", 120, (550 + (i - 1) * 130, 880))

            #enemy
            color = self.black
            for i in range(1, 4):
                if i == self.step:
                    color = self.blue
                pos_img_x = 475 + (i - 1) * 425
                pygame.draw.rect(screen, self.white, (pos_img_x - 15, 25, 150, 170), 0, 15)
                self.image("perudo_images/users/bot.jpg", 120, (pos_img_x, 40))
                len_name = self.len_line(self.names[i], 24)
                pos_line_x = 475 + (i - 1) * 425 + 60 - len_name//2
                self.line(self.names[i], 24, color, (pos_line_x, 170), style=None)
                self.line(f"{self.players_dice[self.names[i]]}", 24, color, (pos_line_x, 190), style=None)
                color = self.black

            for i in (0, 4):
                if i == self.step:
                    color = self.blue
                if i == 0:
                    pygame.draw.rect(screen, self.white, (35, 415, 150, 175), 0, 15)
                    self.image("perudo_images/users/bot.jpg", 120, (50, 430))
                else:
                    pygame.draw.rect(screen, self.white, (1700, 415, 150, 175), 0, 15)
                    self.image("perudo_images/users/bot.jpg", 120, (1750, 430))
                len_name = self.len_line(self.names[i], 24)
                pos_line_x = 475 + (i - 1) * 425 + 60 - len_name//2
                self.line(self.names[i], 24, color, (pos_line_x, 560))
                self.line(f"{self.players_dice[self.names[i]]}", 24, color, (pos_line_x, 580), style=None)
                color = self.black

            if len(self.bet) != 0:
                self.line(f"Ставка: {self.bet["num"]}", 60, self.black, (800, 485))
                self.image(f"perudo_images/dice/dice{self.bet["val"]}.jpg", 50, (1000 + (25 * (len(str(self.bet["num"])) - 1)), 477))

            pygame.display.update()
        
        pygame.quit()

perudo_game = Perudo("РЕП_ИГРОК")
