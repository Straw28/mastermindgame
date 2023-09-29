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

    def give_up(self, user_input):
        if user_input == ["give", "up"]:
            print(f"The secret code was: {', '.join([str(color) for color in self.selected_colors])}")
            self.game_over = True
            return self.game_over
    
    def is_game_over(self):
        return self.game_over  or self.MAX_TRIES == 0

    def game_won(self, user_guess):
        return all(match == Match.EXACT for match in user_guess)

    def get_user_input(self):
        user_input = input("Enter your guess (e.g., red blue green): ").strip().split()
        return user_input
    
    def valid_input(self, user_input):
        if len(user_input) != len(self.selected_colors):
                print("Invalid guess. Please enter the same number of colors.")
                return False
    
    def transform_input(self, user_input):
        user_provided_colors = [Colors[color.upper()] for color in user_input]
        return user_provided_colors
    
    def print_result_of_guess(self, user_guess):
        print("Result:", user_guess)
    
    def play_game(self):
        while self.MAX_TRIES > 0:
            user_input = self.get_user_input()

            if self.give_up(user_input):
                break

            elif not self.valid_input(user_input):
                continue

            else:
                user_provided_colors = self.transform_input(user_input)
                user_guess = self.guess(self.selected_colors, user_provided_colors)
                self.decrease_tries_remaining()

                self.print_result_of_guess()

                if self.game_won(user_guess):
                    print(f"You won! The code was: {', '.join([str(color) for color in self.selected_colors])}")
                    break

                if self.is_game_over():
                    print(f"Game over! You ran out of tries. The secret code was: {', '.join([str(color) for color in self.selected_colors])}")



if __name__ == "__main__":
    game = MasterMindGame()
    game.play_game()