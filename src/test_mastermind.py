import unittest
from parameterized import parameterized
from mastermind import Colors
from mastermind import Match
from mastermind import MasterMindGame



globals().update( Colors.__members__)
globals().update( Match.__members__)

class MasterMindTests(unittest.TestCase):
  def test_canary(self):
    self.assertTrue(True)


  @parameterized.expand(
      [
        ([YELLOW, RED, GREEN, ORANGE, CYAN, PINK], [YELLOW, RED, GREEN, ORANGE, CYAN, PINK], [EXACT] * 6),
        ([YELLOW, RED, GREEN, ORANGE, CYAN, PINK], [PINK, YELLOW, RED, GREEN, ORANGE, CYAN], [PARTIAL] * 6),
        ([YELLOW, RED, GREEN, ORANGE, CYAN, PINK], [VIOLET, BLUE, TEAL, MAGENTA, BROWN, SKY_BLUE], [UNKNOWN] * 6),
        ([YELLOW, RED, GREEN, ORANGE, CYAN, PINK], [YELLOW, RED, GREEN, ORANGE, BROWN, SKY_BLUE], [EXACT, EXACT, EXACT, EXACT, UNKNOWN, UNKNOWN]),
        ([YELLOW, RED, GREEN, ORANGE, CYAN, PINK], [VIOLET, BLUE, GREEN, ORANGE, CYAN, PINK], [EXACT, EXACT, EXACT, EXACT, UNKNOWN, UNKNOWN]),
        ([YELLOW, RED, GREEN, CYAN, PINK, ORANGE], [YELLOW, RED, GREEN, PINK, ORANGE, CYAN], [EXACT, EXACT, EXACT, PARTIAL, PARTIAL, PARTIAL]),
        ([YELLOW, RED, MAGENTA, CYAN, PINK, ORANGE], [BROWN, RED, GREEN, PINK, ORANGE, CYAN], [EXACT, PARTIAL, PARTIAL, PARTIAL, UNKNOWN, UNKNOWN]),
        ([YELLOW, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW], [YELLOW, RED, GREEN, ORANGE, CYAN, PINK], [EXACT, PARTIAL, PARTIAL, PARTIAL, PARTIAL, PARTIAL]),
        ([YELLOW, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW], [PINK, RED, GREEN, ORANGE, CYAN, YELLOW], [PARTIAL, PARTIAL, PARTIAL, PARTIAL, PARTIAL, EXACT])
      ]
  )

  def test_guess(self, selected_colors, user_provided_colors, expected_response):
    
    game = MasterMindGame()
    response = game.guess(selected_colors, user_provided_colors)

    self.assertEqual(expected_response, response)

 
  def test_max_tries(self):
    
    game = MasterMindGame()
    
    for i in range(game.MAX_TRIES):
      user_guess = game.guess([YELLOW, RED, GREEN, ORANGE, CYAN, PINK], [YELLOW, RED, GREEN, ORANGE, BROWN, SKY_BLUE])
      game.decrease_tries_remaining()

    self.assertEqual(0, game.MAX_TRIES)

  def test_win_game(self):
    
    game = MasterMindGame() 

    user_colors = [YELLOW, RED, GREEN, ORANGE, CYAN, PINK]
    actual_colors = [YELLOW, RED, GREEN, ORANGE, CYAN, PINK]

    response = game.guess(user_colors, actual_colors)
    expected_response = [EXACT] * 6
    
    if game.MAX_TRIES > 0:
      self.assertTrue(response == expected_response)

'''
x guess with the first color in the selected colors repeated five times (six of the same color)
-guess with the last color in the selected colors repeated (six of the same color)
-guess with the first color in the selected colors repeated from position two to six, with first position in the guess having the second color in selection
-guess with the first color in the selected colors repeated from position two to six, with first position in the guess having no match
'''


if __name__ == '__main__': 
  unittest.main()
