from enum import Enum
from collections import Counter

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

def guess(selected_colors, user_provided_colors):
    exact_matches = sum(1 for sel, user in zip(selected_colors, user_provided_colors) if sel == user)
    partial_matches = sum((Counter(selected_colors)& Counter(user_provided_colors)).values())- exact_matches
    unknown_matches = len(selected_colors) - exact_matches - partial_matches



    feedback_string = [Match.EXACT] * exact_matches + [Match.PARTIAL] * partial_matches + [Match.UNKNOWN] * unknown_matches

    return feedback_string
    



