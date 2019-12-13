import unittest
import clauses

class TestClauses(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1_verify_arg(self):
        result = clauses.verify_arg(["test", "1", "2"])
        self.assertEqual(result, (False, -1))


    def test_2_verify_arg(self):
        result = clauses.verify_arg(["test", "a"])
        self.assertEqual(result, (False, -2))

    def test_3_verify_arg(self):
        result = clauses.verify_arg(["test", "1"])
        self.assertEqual(result, (False, -3))

    def test_4_verify_arg(self):
        result = clauses.verify_arg(["test", "100"])
        self.assertEqual(result, (False, -3))

    def test_5_verify_arg(self):#correct
        result = clauses.verify_arg(["test", "2"])
        self.assertEqual(result, (True, 2))

if __name__=='__main__':
    unittest.main()
