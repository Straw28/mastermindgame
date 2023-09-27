import unittest
from parameterized import parameterized
from src.mastermind import guess
from src.mastermind import Colors
from src.mastermind import Match

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
        ([YELLOW, RED, GREEN, ORANGE, CYAN, PINK], [VIOLET, BLUE, GREEN, ORANGE, CYAN, PINK], [UNKNOWN, UNKNOWN, EXACT, EXACT, EXACT, EXACT]),
        ([YELLOW, RED, GREEN, CYAN, PINK, ORANGE], [YELLOW, RED, GREEN, PINK, ORANGE, CYAN], [EXACT, EXACT, EXACT, PARTIAL, PARTIAL, PARTIAL]),
        ([YELLOW, RED, MAGENTA, CYAN, PINK, ORANGE], [BROWN, RED, GREEN, PINK, ORANGE, CYAN], [UNKNOWN, EXACT, UNKNOWN, PARTIAL, PARTIAL, PARTIAL]),
      ]
  )

  def test_guess(self, selected_colors, user_provided_colors, expected_response):
    response = guess(selected_colors, user_provided_colors)
    count_response = [response.count(EXACT), response.count(PARTIAL), response.count(UNKNOWN) ]
    count_expected = [expected_response.count(EXACT), expected_response.count(PARTIAL), expected_response.count(UNKNOWN)]
    
    self.assertEqual(count_expected, count_response)


if __name__ == '__main__': 
  unittest.main()

