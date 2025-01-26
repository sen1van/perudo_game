from random import randint, choice

class BaseBot:
    def __init__(self, cubes):
        self.cubes = cubes
    
    def step(self, bet, dices_count):
        if bet[1] == 1:
            if randint(0, 12) == 0:
                return '<'
            if randint(0, 12) != 1:
                if dices_count / 6 - 1 > bet[0]:
                    return [bet[0] + 1, bet[1]]
                if randint(0, 2) == 0:
                    print((dices_count / 6 - 1))
                    return '<'
                else:
                    return (bet[0] * 2 + 1, randint(1, 6))
            return '=='
        if bet[0] < dices_count / 3 + 1:
            if randint(0, 3) == 0:
                return [bet[0] + 1, randint(1, 6)]
            return [bet[0] + randint(1, 2), bet[1]]
        if randint(0, 3) == 0:
            return [bet[0] + 1, bet[1]]
        if randint(0, 5) == 0:
            return '=='
        return '<'
    
    def first_move(self):
        ch = choice(self.cubes)
        buff = self.cubes.count(ch)
        return (buff + randint(1, 5), ch)