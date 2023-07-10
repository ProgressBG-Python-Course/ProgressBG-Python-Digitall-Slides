# test_example.py
import unittest

def floor_div(x,y):
  return x/y

class PositiveTest(unittest.TestCase):
  def test_floor_div_with_positive_integers(self):
    self.assertEqual(floor_div(4,3), 1)
