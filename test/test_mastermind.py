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

 
  def test_max_tries(self):
    game = MasterMindGame()
    for i in range(game.MAX_TRIES):
      user_guess = game.guess([YELLOW, RED, GREEN, ORANGE, CYAN, PINK], [YELLOW, RED, GREEN, ORANGE, BROWN, SKY_BLUE])
      game.decrease_tries_remaining()

    self.assertTrue(game.is_game_over())

  def test_win_game(self):
    
    game = MasterMindGame() 

    user_colors = [YELLOW, RED, GREEN, ORANGE, CYAN, PINK]
    actual_colors = [YELLOW, RED, GREEN, ORANGE, CYAN, PINK]

    response = game.guess(user_colors, actual_colors)
    
    self.assertTrue(game.game_won(response))

  def test_player_gives_up(self):
    game = MasterMindGame()
    game.give_up()

    self.assertTrue(game.give_up())

  # @patch('sys.stdout', new_callable=StringIO)
  # @patch('builtins.input', side_effect=['red blue green orange cyan pink', 'green yellow pink', 'give up'])
  # def test_play_game(self, mock_input, mock_stdout):
  #     game = MasterMindGame()
  #     game.play_game()

  # @patch('sys.stdout', new_callable=StringIO)
  # @patch('builtins.input', side_effect=['red blue green orange cyan pink'])
  # def test_play_game_user_wins(self, mock_input, mock_stdout):
  #   game = MasterMindGame()
  #   game.selected_colors = [RED, BLUE, GREEN, ORANGE, CYAN, PINK ]
  #   game.play_game()
    
  #   output = mock_stdout.getvalue()

  #   self.assertIn(f"You won! The code was: {', '.join([str(color) for color in game.selected_colors])}", output)

  # @patch('sys.stdout', new_callable=StringIO)
  # @patch('builtins.input', side_effect=['red blue green orange cyan pink', 'red blue green orange cyan pink', 'red blue green orange cyan pink'])
  # def test_play_game_game_over(self, mock_input, mock_stdout):
  #   game = MasterMindGame()
  #   game.MAX_TRIES = 3
  #   game.selected_colors = [GREEN, RED, CYAN, ORANGE, BLUE, VIOLET]
  #   game.play_game()

  #   output = mock_stdout.getvalue()

  #   self.assertIn(f"Game over! You ran out of tries. The secret code was: {', '.join([str(color) for color in game.selected_colors])}", output)

  



if __name__ == '__main__': 
  unittest.main()
