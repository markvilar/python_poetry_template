import unittest

from libtemp.common import concatenate_strings

class MathTests(unittest.TestCase):
    def setUp(self):
        # NOTE: Method to initialize test case components
        pass

    def tearDown(self):
        # NOTE: Method to shut down test case components
        pass

    def test_string_concatenation(self):
        concatenated = concatenate_strings(["hello", " ", "world"])
        self.assertEqual(concatenated, "hello world")

if __name__ == "__main__":
    unittest.main()
