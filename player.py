class Player:
    def __init__(self):
        self.name = ''
        self.chosen_gesture = ''
        self.gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock' ]
        self.score = 0
    
    def get_name(self):
        self.name = input('Enter name')
    
    def choose_gesture(self):
        chosen_gesture = input(f'Select your gesture: {self.gestures[0]}, {self.gestures[1]}, {self.gestures[2]}, {self.gestures[3]}, {self.gestures[4]}')
        if chosen_gesture in self.gestures:
            self.chosen_gesture = chosen_gesture
            print(f'{self.name} has selected {self.choosen_gesture}')
        else:
            self.choose_gesture()

    




    
