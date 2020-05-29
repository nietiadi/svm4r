import unittest
from PLSatProblem import PLSatProblem

class TestPLSatProblemLinux(unittest.TestCase):
    def setUp(self):
        if PLSatProblem.num_propositions == 0:
            PLSatProblem.init_class_properties(2)

    def tearDown(self):
        pass

    def test_1_unsat(self):
        problem = PLSatProblem('0,0,1,0,0,1,0,0')
        my_cal = 'unsat'
        result = problem.create_ctlrp_input();

        self.assertEqual(my_cal, result)

if __name__ == '__main__':
    unittest.main()