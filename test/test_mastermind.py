import unittest
from src.mastermind import guess
from src.mastermind import Colors
from src.mastermind import Match


globals().update(Colors.__members__)
globals().update(Match.__members__)

class MasterMindTests(unittest.TestCase):
  def test_canary(self):
    self.assertTrue(True)

  def test_code_match_mixed_results(self):
    
    selected_colors = [YELLOW, RED, GREEN, ORANGE, CYAN, PINK]

    response = guess(selected_colors, selected_colors)

    self.assertEqual([EXACT]*6, response) 



if __name__ == '__main__': 
  unittest.main()

