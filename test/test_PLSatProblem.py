import unittest
import random
from pl_sat_problem import PLSatProblem


class TestPLSatProblem(unittest.TestCase):



    def setUp(self):
        """
        if PLSatProblem.num_propositions == 0:
            for i in range(0, 10):
                vec = str([str(random.randint(0, 1)) for j in range(1, 9)])
                vec = vec.replace('\'', '')
                vec = vec.replace('[', '')
                vec = vec.replace(']', '')
                vec = vec.replace(' ', '')
                print(vec)
        """
        """
1,1,0,1,0,0,1,0
0,0,0,0,1,1,1,0
1,1,0,1,1,1,1,1
0,0,0,1,1,1,1,1
1,1,1,1,0,1,0,0
0,1,0,1,0,0,0,0
1,0,0,0,1,0,1,1
0,1,1,1,1,1,0,0
0,0,1,1,0,0,0,1
0,1,1,1,1,0,1,0
        """
        if PLSatProblem.num_propositions == 0:
            PLSatProblem.init_class_properties(2)

    def tearDown(self):
        pass

    def test_0_create_ctlrp_input_body(self):
        problem = PLSatProblem('0,0,0,0,0,0,0,1')
        my_cal = 'or(not(p0),not(p1))'
        result = problem.create_ctlrp_input_body()
        self.assertEqual(my_cal, result)

    def test_1_create_ctlrp_input_body(self):
        problem = PLSatProblem('1,0,0,0,0,0,0,1')
        my_cal = 'p1,or(not(p0),not(p1))'
        result = problem.create_ctlrp_input_body()
        self.assertEqual(my_cal, result)

    def test_2_create_ctlrp_input_body(self):
        problem = PLSatProblem('1,1,0,1,0,0,1,0')
        my_cal = 'p1,not(p1),or(p0,p1),or(not(p0),p1)'
        result = problem.create_ctlrp_input_body()
        self.assertEqual(my_cal, result)

    def test_3_create_ctlrp_input_body(self):
        problem = PLSatProblem('0,0,0,0,1,1,1,0')
        my_cal = 'or(p0,not(p1)),not(p0),or(not(p0),p1)'
        result = problem.create_ctlrp_input_body()
        self.assertEqual(my_cal, result)

    def test_4_create_ctlrp_input_body(self):
        problem = PLSatProblem('1,1,0,1,1,1,1,1')
        my_cal = 'p1,not(p1),or(p0,p1),or(p0,not(p1)),not(p0),or(not(p0),p1),or(not(p0),not(p1))'
        result = problem.create_ctlrp_input_body()
        self.assertEqual(my_cal, result)

    def test_5_create_ctlrp_input_body(self):
        problem = PLSatProblem('0,0,0,1,1,1,1,1')
        my_cal = 'or(p0,p1),or(p0,not(p1)),not(p0),or(not(p0),p1),or(not(p0),not(p1))'
        result = problem.create_ctlrp_input_body()
        self.assertEqual(my_cal, result)

    def test_6_create_ctlrp_input_body(self):
        problem = PLSatProblem('1,1,1,1,0,1,0,0')
        my_cal = 'p1,not(p1),p0,or(p0,p1),not(p0)'
        result = problem.create_ctlrp_input_body()
        self.assertEqual(my_cal, result)

    def test_7_create_ctlrp_input_body(self):
        problem = PLSatProblem('0,1,0,1,0,0,0,0')
        my_cal = 'not(p1),or(p0,p1)'
        result = problem.create_ctlrp_input_body()
        self.assertEqual(my_cal, result)

    def test_8_create_ctlrp_input_body(self):
        problem = PLSatProblem('1,0,0,0,1,0,1,1')
        my_cal = 'p1,or(p0,not(p1)),or(not(p0),p1),or(not(p0),not(p1))'
        result = problem.create_ctlrp_input_body()
        self.assertEqual(my_cal, result)

    def test_9_create_ctlrp_input_body(self):
        problem = PLSatProblem('0,1,1,1,1,1,0,0')
        my_cal = 'not(p1),p0,or(p0,p1),or(p0,not(p1)),not(p0)'
        result = problem.create_ctlrp_input_body()
        self.assertEqual(my_cal, result)

    def test_10_create_ctlrp_input_body(self):
        problem = PLSatProblem('0,0,1,1,0,0,0,1')
        my_cal = 'p0,or(p0,p1),or(not(p0),not(p1))'
        result = problem.create_ctlrp_input_body()
        self.assertEqual(my_cal, result)

    def test_11_create_ctlrp_input_body(self):
        problem = PLSatProblem('0,1,1,1,1,0,1,0')
        my_cal = 'not(p1),p0,or(p0,p1),or(p0,not(p1)),or(not(p0),p1)'
        result = problem.create_ctlrp_input_body()
        self.assertEqual(my_cal, result)


if __name__ == '__main__':
    unittest.main()