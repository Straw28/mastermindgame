from enum import Enum

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

def guess(user_guess, actual_color_code):
    correct_guesses = [''] * len(actual_color_code) 
    
    for i in range(len(actual_color_code)):
        if user_guess[i] == actual_color_code[i]:
            correct_guesses[i] = Match.EXACT
        elif user_guess[i] in actual_color_code:
            correct_guesses[i] = Match.PARTIAL
        else:
            correct_guesses[i] = Match.UNKNOWN
      
    return correct_guesses
    



