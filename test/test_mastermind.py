import unittest
from src.mastermind import guess
from src.mastermind import Colors
from src.mastermind import Match

globals().update(Colors.__members__)
globals().update(Match.__members__)

class MasterMindTests(unittest.TestCase):
  def test_canary(self):
    self.assertTrue(True)

  def test_code_match_all_correct_results(self):
    
    selected_colors = [Colors.YELLOW, Colors.RED, Colors.GREEN, Colors.ORANGE, Colors.CYAN, Colors.PINK]

    response = guess(selected_colors, selected_colors)

    self.assertEqual([Match.EXACT] * 6, response) 

  def test_code_match_all_silver_results(self):
    
    selected_colors = [Colors.YELLOW, Colors.RED, Colors.GREEN, Colors.ORANGE, Colors.CYAN, Colors.PINK]

    response = guess(selected_colors, selected_colors[::-1])

    self.assertEqual([Match.PARTIAL] * 6, response)

if __name__ == '__main__': 
  unittest.main()

