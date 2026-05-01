import unittest
from sample_code import bad_function

class TestSample(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(bad_function(3), 6)

    def test_case_2(self):
        self.assertEqual(bad_function(5), 20)

if __name__ == "__main__":
    unittest.main()