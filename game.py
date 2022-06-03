from human import Human
from ai import Ai


class Game:
    def __init__(self):
        self.player1 = Human()
        self.player2 = None
    
    def run_game(self):
        self.display_greeting()
        self.game_rules()
        self.choose_game_type()

        
    
    
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

    def choose_game_type(self):
        while True:
            try:
                game_type = int(input('Choose 1 for player vs player or choose 2 for player vs ai'))
            except ValueError:
                    continue
            if game_type == 1:
                self.player2 = Human()
                self.player1.get_name()
                print(f'Hi {self.player1.name}.')
                self.player2.get_name()
                print(f'Hi {self.player2.name}')
                print(f'{self.player1.name} vs {self.player2.name}')
                break
            elif game_type == 2:
                self.player2 = Ai()
                self.player1.get_name()
                print(f'Hi {self.player1.name}')
                self.player2.get_name()
                print(f'Hi {self.player2.name}')
                print(f'{self.player1.name} vs {self.player2.name}')
                break
    def game_round(self):
        while self.player1.score < 2 and self.player2.score < 2:
            print('Round 2:')
            self.player1.choose_gesture()
            self.player2.choose_gesture()
            if self.player1.chosen_gesture == self.player2.chosen_gesture:
                print('Tied round')
            elif self.player1.chosen_gesture == self.player1.gestures[0] and self.player2.chosen_gesture == self.player2.gestures[2]:
                print(f'{self.player1.name} wins the round.')
                self.player_one.score += 1
            elif self.player1.chosen_gesture == self.player1.gestures[0] and self.player2.chosen_gesture == self.player2.gestures[3]:
                print(f'{self.player1.name} wins the round.')
                self.player_one.score += 1
            elif self.player1.chosen_gesture == self.player1.gestures[1] and self.player2.chosen_gesture == self.player2.gestures[0]:
                print(f'{self.player1.name} wins the round.')
                self.player_one.score += 1
            elif self.player1.chosen_gesture == self.player1.gestures[1] and self.player2.chosen_gesture == self.player2.gestures[4]:
                print(f'{self.player1.name} wins the round.')
                self.player_one.score += 1
            elif self.player1.chosen_gesture == self.player1.gestures[2] and self.player2.chosen_gesture == self.player2.gestures[1]:
                print(f'{self.player1.name} wins the round.')
                self.player_one.score += 1
            elif self.player1.chosen_gesture == self.player1.gestures[2] and self.player2.chosen_gesture == self.player2.gestures[3]:
                print(f'{self.player1.name} wins the round.')
                self.player_one.score += 1
            elif self.player1.chosen_gesture == self.player1.gestures[3] and self.player2.chosen_gesture == self.player2.gestures[1]:
                print(f'{self.player1.name} wins the round.')
                self.player_one.score += 1
            elif self.player1.chosen_gesture == self.player1.gestures[3] and self.player2.chosen_gesture == self.player2.gestures[4]:
                print(f'{self.player1.name} wins the round.')
                self.player_one.score += 1
            elif self.player1.chosen_gesture == self.player1.gestures[4] and self.player2.chosen_gesture == self.player2.gestures[0]:
                print(f'{self.player1.name} wins the round.')
                self.player_one.score += 1
            elif self.player1.chosen_gesture == self.player1.gestures[4] and self.player2.chosen_gesture == self.player2.gestures[2]:
                print(f'{self.player1.name} wins the round.')
                self.player_one.score += 1
            else:
                print(f'Scoreboard:  {self.player1.name}: {self.player1.score}.  {self.player1.name}: {self.player2.score}.')
                









    

