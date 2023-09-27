import unittest
from parameterized import parameterized
from mastermind import guess
from mastermind import Colors
from mastermind import Match


globals().update( Colors.__members__)
globals().update( Match.__members__)

class MasterMindTests(unittest.TestCase):
  def test_canary(self):
    self.assertTrue(True)

  # def test_code_match_all_black_results(self):
    
  #   selected_colors = [YELLOW, RED, GREEN, ORANGE, CYAN, PINK]

  #   response = guess(selected_colors, selected_colors)

  #   self.assertEqual([EXACT] * 6, response) 

  # def test_code_match_all_silver_results(self):
    
  #   selected_colors = [YELLOW, RED, GREEN, ORANGE, CYAN, PINK]
  #   user_provided_colors = [PINK, YELLOW, RED, GREEN, ORANGE, CYAN]
    
  #   response = guess(selected_colors, user_provided_colors)

  #   self.assertEqual([PARTIAL] * 6, response)

  # def test_code_match_no_colors_guessed(self):
  #   selected_colors = [YELLOW,  RED,  GREEN,  ORANGE,  CYAN,  PINK]
  #   user_provided_colors = [ VIOLET,  BLUE,  TEAL,  MAGENTA,  BROWN,  SKY_BLUE]

  #   response = guess(selected_colors, user_provided_colors)

  #   self.assertEqual([UNKNOWN] * 6, response)

  # def test_code_match_first_four_match(self):
  #   selected_colors = [YELLOW,  RED,  GREEN,  ORANGE,  CYAN,  PINK]
  #   user_provided_colors = [ YELLOW,  RED,  GREEN,  ORANGE,  BROWN,  SKY_BLUE]

  #   response = guess(selected_colors, user_provided_colors)

  #   expected_response = [EXACT,  EXACT,  EXACT,  EXACT,  UNKNOWN,  UNKNOWN]
    
  #   self.assertEqual(expected_response, response)  


  # def test_code_match_last_four_match(self):
  #   selected_colors = [YELLOW,  RED,  GREEN,  ORANGE,  CYAN,  PINK]
  #   user_provided_colors = [VIOLET,  BLUE,  GREEN,  ORANGE,  CYAN,  PINK]

  #   response = guess(selected_colors, user_provided_colors)

  #   expected_response = [UNKNOWN,  UNKNOWN,  EXACT,  EXACT,  EXACT,  EXACT]
    
  #   self.assertEqual(expected_response, response)  

  # def test_code_match_first_three_match_rest_silver(self):
  #   selected_colors = [YELLOW,  RED,  GREEN,  CYAN,  PINK,  ORANGE]
  #   user_provided_colors = [YELLOW,  RED,  GREEN,  PINK,  ORANGE,  CYAN]

  #   response = guess(selected_colors, user_provided_colors)

  #   expected_response = [EXACT,  EXACT,  EXACT,  PARTIAL,  PARTIAL,  PARTIAL]
    
  #   self.assertEqual(expected_response, response) 

  # def test_code_match_first_and_third_mismatch_second_match_rest_silver(self):
  #   selected_colors = [YELLOW,  RED,  MAGENTA,  CYAN,  PINK,  ORANGE]
  #   user_provided_colors = [BROWN,  RED,  GREEN,  PINK,  ORANGE,  CYAN]

  #   response = guess(selected_colors, user_provided_colors)

  #   expected_response = [UNKNOWN,  EXACT,  UNKNOWN,  PARTIAL,  PARTIAL,  PARTIAL]
    
  #   self.assertEqual(expected_response, response) 

@parameterized.expand(
    [
      ([YELLOW, RED, GREEN, ORANGE, CYAN, PINK], [YELLOW, RED, GREEN, ORANGE, CYAN, PINK], [EXACT] * 6),
            ([YELLOW, RED, GREEN, ORANGE, CYAN, PINK], [PINK, YELLOW, RED, GREEN, ORANGE, CYAN], [PARTIAL] * 6),
            ([YELLOW, RED, GREEN, ORANGE, CYAN, PINK], [VIOLET, BLUE, TEAL, MAGENTA, BROWN, SKY_BLUE], [UNKNOWN] * 6),
            ([YELLOW, RED, GREEN, ORANGE, CYAN, PINK], [YELLOW, RED, GREEN, ORANGE, BROWN, SKY_BLUE], [EXACT, EXACT, EXACT, EXACT, UNKNOWN, UNKNOWN]),
            ([YELLOW, RED, GREEN, ORANGE, CYAN, PINK], [VIOLET, BLUE, GREEN, ORANGE, CYAN, PINK], [EXACT, EXACT, EXACT, EXACT, UNKNOWN, UNKNOWN]),
            ([YELLOW, RED, GREEN, CYAN, PINK, ORANGE], [YELLOW, RED, GREEN, PINK, ORANGE, CYAN], [EXACT, EXACT, EXACT, PARTIAL, PARTIAL, PARTIAL]),
            ([YELLOW, RED, MAGENTA, CYAN, PINK, ORANGE], [BROWN, RED, GREEN, PINK, ORANGE, CYAN], [UNKNOWN, EXACT, UNKNOWN, PARTIAL, PARTIAL, PARTIAL]),
    ],
)

def test_guess(self, selected_colors, user_provided_colors, expected_response):
  response = guess(selected_colors, user_provided_colors)

  self.assertEqual(expected_response, response)


if __name__ == '__main__': 
  unittest.main()

