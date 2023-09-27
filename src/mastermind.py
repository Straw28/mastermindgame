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
    exact_count = 0
    partial_count = 0
    unknown_count = 0

    for i in range(len(actual_color_code)):
        if user_guess[i] == actual_color_code[i]:
            exact_count += 1
        elif user_guess[i] in actual_color_code and user_guess[i] != actual_color_code[i]:
            partial_count += 1
        else:
            unknown_count += 1


    feedback_string = [Match.EXACT] * exact_count + [Match.PARTIAL] * partial_count + [Match.UNKNOWN] * unknown_count

    return feedback_string
    



