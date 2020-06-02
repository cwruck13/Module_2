import unittest
from main import camper_age_input as cai

#testing method
class FunctionTestCase(unittest.TestCase):
    def test_12_years_to_months(self):
        #12 years old should be 144 months old
        self.assertEqual(144, cai.convert_to_months(12))

    def test_5_years_to_months(self):
        #5 years old should be 60 months old
        self.assertEqual(60, cai.convert_to_months(5))

    def test_16_years_to_months(self):
        #16 years old should be 192 months old
        self.assertEqual(192, cai.convert_to_months(16))


if __name__ == '__main__':
    unittest.main()
