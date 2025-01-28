from pygame import Vector2, draw, surface, draw, Rect
from pygame.locals import *
import random

from bots import BaseBot
from utils import draw_text, draw_text_center, draw_image

class Perudo:
    def __init__(self, font):
        self.size = Vector2(1200, 800)
        
        self.icon = '⚀⚁⚂⚃⚄⚅'
        
        self.cursor_pos = Vector2()
        self.cursor_vel = Vector2()
        self.draw_cursor = True
        
        self.cursor_size = 15
        self.cursor_default= 15
        
        self.mouse_pos = Vector2()
        self.mouse_down = False
        
        self.is_bet_updater_open = False
        self.bet_updater_state = [1, 1]
        
        self.font = font
        
        self.buttons = dict()
        self.base_size = 24
        self.selected_size = 36
        
        self.player_turn = 0
        self.players_cubes = dict()
        self.players_cubes_count = dict()
        
        self.cur_bet = [0, 0]
        
        self.display = ''
        self.game_state = 'first move'
        self.game_state_cooldown = 0
        self.bot_cooldown = 0
        
        for i in range(6):
            self.players_cubes_count[i] = 6
        self.reroll_cubes()
        
        self.bots = [((50, self.size.y / 3), 'Робот'),
                     ((self.size.x / 4 - 50, 50), 'Ботик'),
                     ((self.size.x / 4 * 2 - 50, 50), 'Компьютер'),
                     ((self.size.x / 4 * 3 - 50, 50), 'Бот'),
                     ((self.size.x - 100 - 25, self.size.y / 3), 'Ботяра')]
        
        self.canvas = surface.Surface(self.size, SRCALPHA)
        
    def reroll_cubes(self):
        for i in range(6):
            self.players_cubes[i] = [random.randint(1, 6) for i in range(self.players_cubes_count[i])]
    
    def draw_button(self, button_text, button_pos):
        if button_text not in self.buttons:
            self.buttons[button_text] = [self.base_size, 0]
        button_pos = (button_pos[0], button_pos[1] - self.buttons[button_text][0] + self.base_size)
        text_col = draw_text(self.canvas, self.font, button_text, self.buttons[button_text][0], button_pos)
        if text_col.collidepoint(self.mouse_pos):
            self.buttons[button_text][1] -= (self.buttons[button_text][0] - self.selected_size) * 2
            self.buttons[button_text][1] *= 0.3
            self.buttons[button_text][0] += int(self.buttons[button_text][1])
            self.draw_cursor = False
            if self.mouse_event == 1:
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
            if self.mouse_event == 1:
                return True
        else:
            self.buttons[button_text][1] -= (self.buttons[button_text][0] - self.base_size) * 0.5
            self.buttons[button_text][1] *= 0.3
            self.buttons[button_text][0] += int(self.buttons[button_text][1])
        return False
    
    def draw_avatar(self, pos, nickname, cube_count=0):
        pos = Vector2(*pos)
        draw_image(self.canvas, 'perudo_images/users/bot.jpg', pos, 80)
        draw_text_center(self.canvas, self.font, nickname, self.base_size, pos + Vector2(40, 80))
        if cube_count == 0:
            draw_text_center(self.canvas, self.font, 'X', 200, pos + Vector2(40, -100))
        else:
            draw_text_center(self.canvas, self.font, str(cube_count), self.base_size, pos + Vector2(40, 110))
    
    def draw_cubes(self, pos, cubes):
        pos = Vector2(*pos)
        for i in enumerate(cubes):
            draw_image(self.canvas, f'perudo_images/dice/dice{i[1]}.jpg', pos + Vector2(124 * i[0], 0), 104)
    
    def end_move(self):
        self.player_turn += 1
        self.player_turn %= 6
        self.bot_cooldown = 60 * 2

    def end_checkmove(self):
        self.game_state_cooldown = 60 * 5
    
    def draw_bet_updater(self):
        rect = (self.size.x / 9 * 3, self.size.y / 4 * 2, self.size.x / 9 * 3, self.size.y / 4)
        draw.rect(self.canvas, 'white', rect)
        draw.rect(self.canvas, 'black', rect, 4)
        if self.mouse_event == 5:
            if self.mouse_pos.x > self.size.x / 2:
                self.bet_updater_state[1] = max(self.bet_updater_state[1] - 1, 1)
            else:
                self.bet_updater_state[0] = max(self.bet_updater_state[0] - 1, 1)
        if self.mouse_event == 4:
            if self.mouse_pos.x > self.size.x / 2:
                self.bet_updater_state[1] = min(self.bet_updater_state[1] + 1, 6)
            else:
                self.bet_updater_state[0] = min(self.bet_updater_state[0] + 1, 36)
        self.draw_cubes((rect[0] + rect[2] - 194,rect[1] + 20), [self.bet_updater_state[1]])
        draw_text_center(self.canvas, self.font, str(self.bet_updater_state[0]), 80, (rect[0] + 129, rect[1] + 25))
        if self.draw_button_center('X', (rect[0] + 30, rect[1] + 20)):
            self.is_bet_updater_open = False
        if self.draw_button_center('Подтвердить', (rect[0] + 200, rect[1] + 145)):
            if self.game_state == 'first move':
                self.cur_bet = self.bet_updater_state
                self.game_state = 'just move'
                self.end_move()
                return
            if self.game_state == 'just move':
                if self.cur_bet[0] < self.bet_updater_state[0]:
                    self.cur_bet = self.bet_updater_state
                    self.end_move()
                    return
                if self.cur_bet[0] == self.bet_updater_state[0]:
                    if self.cur_bet[1] < self.bet_updater_state[1]:
                        self.cur_bet = self.bet_updater_state
                        self.end_move()
                        return
                    if self.bet_updater_state[1] == 1:
                        if self.cur_bet[1] != 1:
                            self.cur_bet = self.bet_updater_state
                            self.end_move()
                            return
                if self.cur_bet[0] > self.bet_updater_state[0]:
                    if self.cur_bet[1] != 1 and self.bet_updater_state[1] == 1:
                        if int(self.cur_bet[0] / 2 + 0.5) <= self.bet_updater_state[0]:
                            self.cur_bet = self.bet_updater_state
                            self.end_move()
                            return

    def calc(self, dice_num):
        buff = []
        for i in range(6):
            buff += self.players_cubes[i]
        print(buff)
        answ = buff.count(dice_num)
        if dice_num != 1:
            answ += buff.count(1)
        return answ

    def check_equal(self):
        calced = self.calc(self.cur_bet[1])
        print(calced)
        if calced != self.cur_bet[0]:
            self.players_cubes_count[self.player_turn] -= 1
        else:
            self.players_cubes_count[self.player_turn] = min(self.players_cubes_count[self.player_turn] + 1, 6)
        self.game_state = 'check =='
        self.game_state_cooldown = 5000
        
    def check_lower(self):
        last_player = self.player_turn - 1
        if last_player < 0:
            last_player = 5
        while self.players_cubes_count[last_player] == 0:
            last_player = last_player - 1
            if last_player < 0:
                last_player = 5
        calced = self.calc(self.cur_bet[1])
        print(calced)
        if calced >= self.cur_bet[0]:
            self.players_cubes_count[self.player_turn] -= 1
        else:
            self.players_cubes_count[last_player] -= 1
            self.player_turn = last_player
        self.game_state = 'check <'
        self.game_state_cooldown = 5000
    
    def show_display(self):
        draw_text_center(self.canvas, self.font, self.display, 60, (self.size.x / 2, self.size.y / 4))
    
    def show_cubes(self):
        for i in range(6):
            buff = ''
            for cube in self.players_cubes[i]:
                buff += self.icon[cube - 1]
            draw_text_center(self.canvas, self.font, buff, 40, (self.size.x / 2, self.size.y / 5 * 2 + i * 37))
    
    def bot_just_move(self):
        print(self.players_cubes[self.player_turn], sum([self.players_cubes_count[i] for i in range(6)]), self.cur_bet)
        bot = BaseBot(self.players_cubes[self.player_turn])
        move = bot.step(self.cur_bet, sum([self.players_cubes_count[i] for i in range(6)]))
        if move == '<':
            self.check_lower()
            self.end_checkmove()
            return
        if move == '==':
            self.check_equal()
            self.end_checkmove()
            return
        self.cur_bet = move
        self.end_move()

    def bot_first_move(self):
        print(self.players_cubes[self.player_turn], sum([self.players_cubes_count[i] for i in range(6)]), self.cur_bet)
        bot = BaseBot(self.players_cubes[self.player_turn])
        move = bot.first_move()
        self.game_state = 'just move'
        self.cur_bet = move
        self.end_move()
        
    def render(self, mouse_pos,  mouse_event):
        self.mouse_pos = mouse_pos
        self.mouse_event = mouse_event
        self.canvas.fill('white')
        
        if self.game_state == 'just move':
            self.display = f'Ставка: {self.cur_bet[0]}' + self.icon[self.cur_bet[1] - 1]
        if self.game_state == 'first move':
            self.display = 'Первая ставка'
        if self.game_state == 'check ==':
            self.display = f'== {self.cur_bet[0]}' + self.icon[self.cur_bet[1] - 1]
            self.show_cubes()
        if self.game_state == 'check <':
            self.display = f'< {self.cur_bet[0]}' + self.icon[self.cur_bet[1] - 1]
            self.show_cubes()
            
        self.show_display()
        
        events = []
        # print(mouse_pos)
        if self.game_state in ['check ==', 'check <'] and self.game_state_cooldown <= 0:
            self.game_state = 'first move'
            self.reroll_cubes()
            
        if self.player_turn != 0:
            while self.players_cubes_count[self.player_turn] == 0:
                self.end_move()
        if self.player_turn != 0 and self.bot_cooldown == 0:
            if self.players_cubes_count[self.player_turn] == 0:
                self.end_move()
            elif self.game_state == 'just move':
                self.bot_just_move()
            elif self.game_state == 'first move':
                self.bot_first_move()
                
        for i in enumerate(self.bots):
            if i[0] + 1 == self.player_turn:
                draw.rect(self.canvas, 'red', (i[1][0][0] - 5, i[1][0][1] - 5, 90, 90), 0, 3)
            self.draw_avatar(i[1][0], i[1][1], self.players_cubes_count[i[0] + 1])
            
        self.draw_cubes((900 - 124 * 6 + 24 - 50, 700 - 80), self.players_cubes[0])
        
        if self.players_cubes_count[0] > 0:
            if self.draw_button('Не верю!', (900, 620)) and self.player_turn == 0 and self.game_state == 'just move':
                self.check_lower()
                self.end_checkmove()
            if self.draw_button('Ровно!', (900, 660)) and self.player_turn == 0 and self.game_state == 'just move':
                self.check_equal()
                self.end_checkmove()
            if self.draw_button('Поднять ставку', (900, 700)):
                self.is_bet_updater_open = True
            if self.is_bet_updater_open and self.game_state in ['just move', 'first move'] and self.player_turn == 0:
                self.draw_bet_updater()
            else:
                self.is_bet_updater_open = False
        elif self.player_turn == 0:
            self.end_move()
        
        if self.bot_cooldown > 0:
            self.bot_cooldown -= 1
        
        if self.game_state_cooldown > 0:
            self.game_state_cooldown -= 1
        
        gamers = 0
        last = 0
        for i in range(6):
            if self.players_cubes_count[i] != 0:
                gamers += 1
                last = i
        if gamers <= 1:
            events.append('game over')
            if last == 0:
                events.append(f'Вы выиграли')
            else:
                events.append('Выиграл: ' + self.bots[i - 1][1])
                
        return (self.canvas, events)