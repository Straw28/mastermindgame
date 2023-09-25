from enum import Enum

class Colors(Enum):
    YELLOW = 'yellow'
    RED = 'red'
    GREEN = 'green'
    ORANGE = 'orange'
    CYAN = 'cyan'
    PINK = 'pink'
    VIOLET = 'violet'
    BLACK = 'black'
    SILVER = 'silver'

def code_match(user_guess, actual_color_code):

    correct_guesses = [''] * len(actual_color_code) 
    
    for i in range(len(actual_color_code)):
        if user_guess[i] == actual_color_code[i]:
            correct_guesses[i] = Colors.BLACK
        elif user_guess[i] in actual_color_code:
            correct_guesses[i] = Colors.SILVER
        else:
            correct_guesses[i] = ''  
    
    return correct_guesses




