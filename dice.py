from random import randint

class one_dice:
    '''This is a class for one dice'''
    def __init__(self) -> None:
        self.rolls: list = []
        self.sixes:int = 0# 1, 2
        self.allowed_s = 2# greater than 2 error
        pass

    def gen_rolls(self):
        temp = 0
        while(True):
            temp = randint(1, 6)
            if temp == 6 and self.sixes < self.allowed_s: 
                self.rolls.append(temp)# gen the roll
                self.sixes += 1
            elif temp != 6:
                self.rolls.append(temp)
                break
    
    def clean(self):
        self.rolls = []
        self.sixes = 0

    def show_rolls(self):
        return self.rolls

class two_dice:
    '''This is a class for two dices'''
    def __init__(self) -> None:
        self.rolls:list = []
        self.allowed_s:int = 2
        self.sixes = 0
    
    def gen_rolls(self):
        temp_1 = 0
        temp_2 = 0
        while(True):
            temp_1, temp_2 = randint(1, 6), randint(1, 6)
            if(temp_1 == 6 and temp_2 == 6) and (self.sixes < self.allowed_s):
                self.rolls.append(temp_1)
                self.rolls.append(temp_2)
            elif (temp_1 != 6 or temp_2 != 6):
                self.rolls.append(temp_1)
                self.rolls.append(temp_2)
                break
            else:
                break
    def clean(self):
        self.rolls = []
        self.sixes = 0

    def show_rolls(self):
        return self.rolls
