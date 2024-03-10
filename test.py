import unittest
from file1 import func

class TestFunc(unittest.TestCase):
    def test_func_1(self):
        self.assertEqual(func(5, 7), 12)

    def test_func_2(self):
        self.assertEqual(func(-4, -3), -3)

    def test_func_3(self):
        self.assertEqual(func(0, 1), 1)

if __name__ == '__main__':
    unittest.main()
