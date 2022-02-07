import unittest
from unittest.mock import MagicMock
import unittest
import sample


class SquareTest(unittest.TestCase):

    def test_get_area(self):
        square = sample.Square()

        x = 1
        expected = 1
        actual = square.get_area(x)
        self.assertEqual(actual, expected)

        x = 2
        expected = 4
        actual = square.get_area(x)
        self.assertEqual(actual, expected)


unittest.main()