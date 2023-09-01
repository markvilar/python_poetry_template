""" Test module for common functions. """

import unittest

from libtemp.common import concatenate_strings

class CommonTests(unittest.TestCase):
    """ Test case for the template library common functions. """

    def setUp(self) -> None:
        """ Method to initialize test case components. """

    def tearDown(self) -> None:
        """ Method to shut down test case components. """

    def test_string_concatenation(self):
        """ Test string concatenation function. """
        concatenated = concatenate_strings(["hello", " ", "world"])
        self.assertEqual(concatenated, "hello world")

if __name__ == "__main__":
    unittest.main()
