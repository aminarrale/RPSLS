from human import Human
from ai import Ai


class Game:
    def __init__(self):
        self.player1 = Human()
        self.player2 = None
    
    def run_game(self):
        self.display_greeting()
        self.game_rules()

        
    
    
    def display_greeting(self):
        print('Welcome to Rock Paper Scissors Lizard Spock.')
        print('each match will be the best of three games')


    def game_rules(self):
        print('Here are the rules to the game:')
        print('Rock crushes Scissors')
        print('Scissors cuts Paper')
        print('Paper covers Rock')
        print('Rock crushes Lizard')
        print('Lizard poisons Spock')
        print('Spock smashes Scissors')
        print('Lizard eats Paper')
        print('Paper disproves Spock')
        print('Spock vaporizes spock')





    

