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
        ([YELLOW, RED, MAGENTA, CYAN, PINK, ORANGE], [YELLOW, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW], [EXACT, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN]),
        ([YELLOW, RED, MAGENTA, CYAN, PINK, ORANGE], [ORANGE, ORANGE, ORANGE, ORANGE, ORANGE, ORANGE], [EXACT, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN]),
        ([YELLOW, RED, MAGENTA, CYAN, PINK, ORANGE], [RED, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW], [PARTIAL, PARTIAL, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN]),
        ([YELLOW, RED, MAGENTA, CYAN, PINK, ORANGE], [BROWN, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW], [PARTIAL, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN, UNKNOWN])
      ]
  )

  def test_guess(self, selected_colors, user_provided_colors, expected_response):
    response = MasterMindGame.guess(self, selected_colors, user_provided_colors)

    self.assertEqual(expected_response, response)

 
  def test_max_tries(self):
    game = MasterMindGame()
    for i in range(game.MAX_TRIES):
      user_guess = game.guess([YELLOW, RED, GREEN, ORANGE, CYAN, PINK], [YELLOW, RED, GREEN, ORANGE, BROWN, SKY_BLUE])
      game.decrease_tries_remaining()

    self.assertEqual(0, game.MAX_TRIES)



if __name__ == '__main__': 
  unittest.main()
