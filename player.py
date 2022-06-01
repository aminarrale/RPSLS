class Player:
    def __init__(self, choose_gesture):
        self.name = ""
        self.choose_gesture = choose_gesture
        self.gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock' ]
    

    def assign_gesture(self, gesture):
        self.gesture = gesture
        print(f'{self.name} selected {self.gesture}')

    
