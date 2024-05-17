import unittest

from problem1 import Solution_1


class TestSolution1(unittest.TestCase):

    def test_shortestWay(self):
        self.assertEqual(Solution_1.shortestWay("abc", "abcbc"), 2)
        self.assertEqual(Solution_1.shortestWay("abc", "acdbc"), -1)
        self.assertEqual(Solution_1.shortestWay("xyz", "xzyxz"), 3)
        self.assertEqual(Solution_1.shortestWay("abc", "abcabc"), 2)
        self.assertEqual(Solution_1.shortestWay("abc", ""), 0)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
