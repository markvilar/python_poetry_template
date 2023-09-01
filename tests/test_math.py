import unittest

from lib.math import add, multiply

class MathTests(unittest.TestCase):
    def setUp(self):
        # NOTE: Method to initialize test case components
        pass

    def tearDown(self):
        # NOTE: Method to shut down test case components
        pass

    def test_add(self):
        result = add(1.0, 2.0)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 3.0)

    def test_multiply(self):
        result = multiply(1.0, 2.0)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 2.0)

if __name__ == "__main__":
    unittest.main()
