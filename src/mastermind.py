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


class MasterMindGame:
    MAX_TRIES = 20 

    def __init__(self):
        #self.selected_colors = selected_colors
        #self.tries_remaining = MasterMindGame.MAX_TRIES
        self.MAX_TRIES = 20
    def guess(self, selected_colors, user_provided_colors):

        match_for_position = lambda i: (Match.EXACT if selected_colors[i] == user_provided_colors[i]
                                        else Match.PARTIAL if selected_colors[i] in user_provided_colors
                                        else Match.UNKNOWN)
        
        return sorted([match_for_position(i) for i in range(len(user_provided_colors))], key = lambda match: match.value)
    
    # def game_over(self):
    #     return self.tries_remaining == 0
    
    # def is_success(self):
    #     return all(match == Match.EXACT for match in self.guess(self.selected_colors))
    
    # def decrease_tries_remaining(self):
    #     self.tries_remaining -= 1
    



