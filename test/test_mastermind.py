import unittest

from src.mastermind import MasterMind

class MasterMindTests(unittest.TestCase):
  def test_canary(self):
    self.assertTrue(True)

  def test_example_remove_this(self):
    self.assertEqual(1, MasterMind().please_remove_this_sample())

if __name__ == '__main__': 
  unittest.main()