from player import Player
import random



class Ai(Player):
    def __init__(self):
        super().__init__() 

    def get_name(self):
        self.name = 'the AI'

    def choose_gesture(self):
        print(f'Choose')
        

