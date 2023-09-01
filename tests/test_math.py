""" Test module for math functions. """

import unittest

from libtemp.math import add, multiply

class MathTests(unittest.TestCase):
    """ Test case for the template library math functions. """

    def setUp(self) -> None:
        """ Method to initialize test case components. """

    def tearDown(self) -> None:
        """ Method to shut down test case components. """

    def test_add(self) -> None:
        """ Test add function. """
        result = add(1.0, 2.0)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 3.0)

    def test_multiply(self) -> None:
        """ Test multiply function. """
        result = multiply(1.0, 2.0)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 2.0)

if __name__ == "__main__":
    unittest.main()
