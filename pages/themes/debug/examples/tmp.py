import unittest

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

if __name__ == '__main__':
    unittest.main()