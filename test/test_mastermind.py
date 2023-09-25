import unittest
from src.mastermind import guess
from src.mastermind import Colors
from src.mastermind import Match



class MasterMindTests(unittest.TestCase):
  def test_canary(self):
    self.assertTrue(True)

  def test_code_match_mixed_results(self):
    
    selected_colors = [Colors.YELLOW, Colors.RED, Colors.GREEN, Colors.ORANGE, Colors.CYAN, Colors.PINK]

    response = guess(selected_colors, selected_colors)
    
    expected = [Match.EXACT] * len(selected_colors)

    self.assertEqual(expected, response)



if __name__ == '__main__': 
  unittest.main()

