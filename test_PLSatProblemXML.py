import unittest
import ttprover.ttprover as pr
import pl_sat_problem_xml as xml


class TestPLSatProblemXML(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_run_ttprover1(self):
        prover = pr.TruthTableProver(input_string='<and><p0/><not><p0/></not></and>')
        result = prover.run(test_satisfiability=True)
        self.assertEqual('unsat', result)

    def test_run_ttprover2(self):
        prover = pr.TruthTableProver(input_string='<p0/>')
        result = prover.run(test_satisfiability=True)
        self.assertEqual('sat', result)

    def test_convert_all_clauses_to_numbers(self):
        xml.PLSatProblemXML.init_class_properties(2)
        numbers = xml.PLSatProblemXML.all_clauses_in_numbers
        #print(numbers)

        self.assertEqual(3, numbers[0])
        self.assertEqual(9, numbers[1])
        self.assertEqual(2, numbers[2])
        self.assertEqual(6, numbers[3])
        self.assertEqual(18, numbers[4])
        self.assertEqual(4, numbers[5])
        self.assertEqual(12, numbers[6])
        self.assertEqual(36, numbers[7])

    def test_version3(self):
        with open('./data/' + str(xml.PLSatProblemXML.num_propositions) + '_prop_version3_xml.cvs', 'rt') as fin:
            i = 0
            for line in fin:
                print(line)
                if i==0:
                    self.assertEqual('0,0,0,0,0,0,0,36,sat', line)
                elif i==26:
                    self.assertEqual('0,0,0,6,18,0,12,36,unsat', line)
                i+=1
            self.assertGreater(i, 0) # make sure the file is not empty





if __name__ == '__main__':
    unittest.main()