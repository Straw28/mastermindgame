import unittest
from parameterized import parameterized
from src.mastermind import Colors
from src.mastermind import Match
from src.mastermind import MasterMindGame
from unittest.mock import patch
from io import StringIO



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

 
  def test_decrease_tries(self):
    game = MasterMindGame()
    game.MAX_TRIES = 3
    game.decrease_tries_remaining()
    self.assertTrue(game.MAX_TRIES, 2)

  def test_player_gives_up(self):
    game = MasterMindGame()
    self.assertFalse(game.game_over)
    self.assertTrue(game.give_up(['give','up']))
    self.assertTrue(game.game_over)
  
  def test_is_game_over_is_not_over(self):
    game = MasterMindGame()
    self.assertFalse(game.is_game_over())

  def test_is_game_over_max_tries(self):
    game = MasterMindGame()
    game.MAX_TRIES = 0
    self.assertTrue(game.is_game_over())

  def test_game_won(self):
    game = MasterMindGame()
    response = [EXACT] * 6
    self.assertTrue(game.game_won(response))

  def test_game_not_won(self):
    game = MasterMindGame()
    response = [EXACT, EXACT, EXACT, PARTIAL, PARTIAL, PARTIAL]
    self.assertFalse(game.game_won(response))

  @patch('builtins.input', side_effect=['red blue green'])
  def test_get_user_input(self, mock_input):
    game = MasterMindGame()
    user_input = game.get_user_input()
    self.assertEqual(user_input, ['red', 'blue', 'green'])

  def test_valid_input_valid(self):
    game = MasterMindGame()
    user_input = ['red', 'blue', 'green']
    result = game.valid_input(user_input)
    self.assertFalse(result)

  def test_valid_input_invalid(self):
    game = MasterMindGame()
    user_input = ['red', 'blue', 'green', 'orange']
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
      result = game.valid_input(user_input)
    output = mock_stdout.getvalue()
    self.assertIn("Invalid guess. Please enter the same number of colors.", output)
    self.assertFalse(result)
  
  def test_transform_input(self):
    game = MasterMindGame()
    user_input = ['red', 'blue', 'green']
    transformed_input = game.transform_input(user_input)
    expected_transformed_input = [RED, BLUE, GREEN]
    self.assertEqual(transformed_input, expected_transformed_input)

  def test_print_result_of_guess(self):
    game = MasterMindGame()
    feedback = [PARTIAL, PARTIAL, PARTIAL]
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
      game.print_result_of_guess(feedback)
    output = mock_stdout.getvalue()
    self.assertIn("Result:", output)

if __name__ == '__main__': 
  unittest.main()