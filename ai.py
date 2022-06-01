from player import Player
import random



class Ai(Player):
    def __init__(self):
        super().__init__() 

    def get_name(self):
        self.name = 'The AI'

    def choose_gesture(self):
        print(f'Choose your gesture: {self.gestures[0]}, {self.gestures[1]}, {self.gestures[2]}, {self.gestures[3]}, {self.gestures[4]}')
        self.chosen_gesture = random.choice(self.gestures)
        print(f'{self.name} has selected {self.chosen_gesture}.')
        

