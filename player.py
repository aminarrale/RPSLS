class Player:
    def __init__(self, name):
        self.name = name
     

    def select_choice(self, choice):
        self.choice = choice
        print(f'{self.name} selected {self.choice}')
        
    def track_score(self, track_score):
        self.score = track_score

