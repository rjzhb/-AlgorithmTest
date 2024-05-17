import unittest

from problem2 import Solution_2


class TestSolution2(unittest.TestCase):

    def test_check_parentheses(self):
        input_strings = [
            "bge)))))))))",
            "((IIII))))))",
            "()()()()(uuu",
            "))))UUUU((()"
        ]
        expected_output = [
            "   ?????????",
            "        ????",
            "        x   ",
            "????    xx  "
        ]
        self.assertEqual(Solution_2.check_parentheses(input_strings), expected_output)

        input_strings = [
            "(a + b)",
            "(a + b))",
            "((a + b)",
            "((a + b))"
        ]
        expected_output = [
            "       ",
            "       ?",
            "x       ",
            "         "
        ]
        self.assertEqual(Solution_2.check_parentheses(input_strings), expected_output)

        input_strings = [
            "abc",
            "(a + (b * c) - d)",
            "(((())))",
            "((())",
            "()())",
            "a(b)c",
            "((a + b)",
            "(a + b)))"
        ]
        expected_output = [
            '   ',
            '                 ',
            '        ',
            'x    ',
            '    ?',
            '     ',
            'x       ',
            '       ??'
        ]
        self.assertEqual(Solution_2.check_parentheses(input_strings), expected_output)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
