import unittest

def add(x, y):
    return x + y

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(2, -3), -1)

if __name__ == '__main__':
    # If the script is run directly (not imported as a module), the unit tests are executed with:
    unittest.main()

# ...
# ----------------------------------------------------------------------
# Ran 3 tests in 0.000s

# OK