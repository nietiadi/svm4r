import unittest
import PLSatProblemXML
import ttprover.truth_table_prover as pr


class TestPLSatProblemXML(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_run_ttprover1(self):
        result = pr.run('<and><p0/><not><p0/></not></and>')
        self.assertEqual('unsat', result)

    def test_run_ttprover2(self):
        result = pr.run('<p0/>')
        self.assertEqual('sat', result)


if __name__ == '__main__':
    unittest.main()