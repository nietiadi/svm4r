import unittest
import prime_numbers

class TestPrimeNumbers(unittest.TestCase):
    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_generate_100_prime_number(self):
        result_list = prime_numbers.generate_prime_numbers(100)
        self.assertEqual(result_list[0], 2)
        self.assertEqual(result_list[1], 3)


if __name__ == '__main__':
    unittest.main()
