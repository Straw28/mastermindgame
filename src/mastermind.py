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

def guess(selected_colors, user_provided_colors):
    exact_count = 0
    partial_count = 0
    unknown_count = 0

    for i in range(len(selected_colors)):
        if user_provided_colors[i] == selected_colors[i]:
            exact_count += 1
        elif user_provided_colors[i] in selected_colors and user_provided_colors[i] != selected_colors[i]:
            partial_count += 1
        else:
            unknown_count += 1


    feedback_string = [Match.EXACT] * exact_count + [Match.PARTIAL] * partial_count + [Match.UNKNOWN] * unknown_count

    return feedback_string
    



