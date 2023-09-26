from enum import Enum

class Colors(Enum):
    YELLOW = 'yellow'
    RED = 'red'
    GREEN = 'green'
    ORANGE = 'orange'
    CYAN = 'cyan'
    PINK = 'pink'
    VIOLET = 'violet'


class Match(Enum):
    EXACT = 'exact'

def guess(user_guess, actual_color_code):

   return [Match.EXACT] * 6



