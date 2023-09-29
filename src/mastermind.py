from enum import Enum
import random

class Colors(Enum):
    YELLOW = 'yellow'
    RED = 'red'
    GREEN = 'green'
    ORANGE = 'orange'
    CYAN = 'cyan'
    PINK = 'pink'
    VIOLET = 'violet'
    BLUE = 'blue'
    TEAL = 'teal'
    MAGENTA = 'magenta'
    BROWN = 'brown'
    SKY_BLUE = 'sky_blue'


class Match(Enum):
    EXACT = 0
    PARTIAL = 1
    UNKNOWN = 2


class MasterMindGame():
    
    def __init__(self):
        self.MAX_TRIES = 3
        self.game_over = False
        self.selected_colors = random.sample(list(Colors), 6)
    
    def guess(self, selected_colors, user_provided_colors):


        match_for_position = lambda i: (Match.EXACT if selected_colors[i] == user_provided_colors[i]
                                        else Match.PARTIAL if selected_colors[i] in user_provided_colors
                                        else Match.UNKNOWN)
        
        return sorted([match_for_position(i) for i in range(len(user_provided_colors))], key = lambda match: match.value)
    
    
    def decrease_tries_remaining(self):
        self.MAX_TRIES -= 1

    def give_up(self):
        self.game_over = True
        return self.game_over
    
    def is_game_over(self):
        return self.game_over  or self.MAX_TRIES == 0

    def game_won(self, user_guess):
        return all(match == Match.EXACT for match in user_guess)


def play_game():
    game = MasterMindGame() 
 
    while game.MAX_TRIES > 0:
        
        print(game.MAX_TRIES)
        user_input = input("Enter your guess (e.g., red blue green): ").strip().split()
        
        if user_input == ["give", "up"]:
            print(f"The secret code was: {', '.join([str(color) for color in game.selected_colors])}")
            game.give_up()
            break
        
        if len(user_input) != len(game.selected_colors):
            print("Invalid guess. Please enter the same number of colors.")
            continue
        
       
        user_provided_colors = [Colors[color.upper()] for color in user_input]
        
        user_guess = game.guess(game.selected_colors, user_provided_colors)
        game.decrease_tries_remaining()

        print("Result:", user_guess)


        if game.game_won(user_guess): 
            print(f"You won! The code was: {', '.join([str(color) for color in game.selected_colors])}")
            break
    
        if game.is_game_over():
            print(f"Game over! You ran out of tries. The secret code was: {', '.join([str(color) for color in game.selected_colors])}")
        

if __name__ == "__main__":
    play_game()
