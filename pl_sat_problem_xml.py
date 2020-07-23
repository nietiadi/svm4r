"""
Each instance of PLSatProblem represents a propositional logic satisfiability problem.
"""
import csv
import os
import xml.etree.ElementTree as ET
import ttprover.ttprover as ttp

class PLSatProblemXML:

    num_propositions = 0
    all_clauses = None
    all_pl_clauses = None

    @classmethod
    def init_class_properties(cls, num_propositions):
        """
        call this before making any PLSatProblem instance
        :param num_propositions: the total number of propositions in this problem
        """
        cls.num_propositions = num_propositions
        cls.all_clauses = cls.load_all_clauses()
        cls.all_clauses = cls.all_clauses[1:] # Remove the empty clause
        cls.all_pl_clauses = cls.load_all_pl_clauses()


    def __init__(self, selected_clauses):
        """
        Constructor
        :param selected_clauses: a set of clauses
        """
        self.select_clauses = selected_clauses
        self.problem = self.create_xml_input()
        self.sat = None


    @classmethod
    def load_all_clauses(cls):
        with open(cls.get_file_of_all_clauses(), 'rt') as fin:
            #lines = [x.strip() for x in fin.readlines()]
            csvin = csv.reader(fin, delimiter=',')
            lines = [x for x in csvin]
        return lines


    @classmethod
    def load_all_pl_clauses(cls): # Can handld the empty clause
        clauses = [PLSatProblemXML.translate_matrix_into_clauses(x) \
                   for x in cls.all_clauses]
        return clauses

    @classmethod
    def translate_matrix_into_clauses(cls, clause):
        """
        :param clause: e.g. ['1','2']
        :return: <or><p0/><not><p1/></not></or>
        """
        zero = 0
        #create root <or></or>
        root = ET.fromstring('<or></or>')
        #print(root.tag)
        #print(root.attrib)

        for i, x in enumerate(clause):
            if x == '0':
                zero += 1
                continue
            elif x == '1':
                ET.SubElement(root, 'p'+str(i))
            elif x == '2':
                neg = ET.SubElement(root, 'not')
                ET.SubElement(neg, 'p'+str(i))
            else:
                pass

        if zero == len(clause):# all are zeros
            return 'F' #The empty clause
        elif len(clause)-zero == 1:# single proposition
            #return '<or></or>'
            #return ET.fromstring(root[0].tag).tostring()
            #return ET.tostring(root[0], encoding='unicode')
            return root[0]
        else:
            #return '<or></or>'
            #return ET.tostring(root, encoding='unicode')
            return root

    def create_xml_input_body(self):
        root_and = ET.fromstring('<and></and>')
        for i, s in enumerate(self.select_clauses.split(',')):
            if int(s) != 0:
                root_and.append(PLSatProblemXML.all_pl_clauses[i])
        return root_and

    def create_xml_input(self):
        num_zeros = self.select_clauses.count('0')
        len = 3 ** PLSatProblemXML.num_propositions - 1  # no empty clause
        if len-num_zeros == 1:# only one clause is selected, \
            problem = self.create_xml_input_body()
            problem = problem[0] # remove the root of <and>
        else:
            # add <and> as a root
            problem = self.create_xml_input_body()
        return problem

    def check_satisfiability(self):
        self.sat = 'unsatisfiable'
        pass

    @classmethod
    def get_file_of_all_clauses(cls):
        return 'data/clauses_for_'+str(cls.num_propositions)+'_propositions.csv'


    def run_ttprover(self):
        problem_str = ET.tostring(self.problem, encoding='unicode')
        prover = ttp.TruthTableProver(input_string=problem_str)
        self.sat = prover.run(test_satisfiability=True)


# for testing
    """
if __name__ == '__main__':
    PLSatProblem.init_class_properties(2)

    problem = PLSatProblem('1,0,0,0,0,0,0,0,0,1')
    for i, (c, pl) in enumerate(zip(problem.all_clauses, problem.all_pl_clauses), start=1):
        print(i, c, pl)

    problem = PLSatProblem('1,0,0,0,0,0,0,1')
    print(problem.problem)
    #for i, (c, pl) in enumerate(zip(problem.all_clauses, problem.all_pl_clauses), start=1):
        #print(i, c, pl)
    #print(str(problem.load_all_clauses()))
    #print(str(problem.load_all_pl_clauses()))
    #print(PLSatProblem.translate_matrix_into_clauses(['0', '0']))
    #print(PLSatProblem.translate_matrix_into_clauses(['1', '2']))
    #print(PLSatProblem.translate_matrix_into_clauses(['0', '2']))
    #print(PLSatProblem.translate_matrix_into_clauses(['2', '0']))

    problem = PLSatProblem('1,1,1,1,1,1,1,1')
    print(problem.problem)
    """

if __name__ == '__main__':
    no_prop = 2
    PLSatProblemXML.init_class_properties(no_prop)

    version = 2

    # write the simple version of data for ML
    # row number + satisfiability
    if version == 1:
        row = 0
        with open('./data/'+str(no_prop)+'_prop_version1_xml.cvs', 'wt') as fout:
            with open('./data/list_of_clause_sets_containing_2_' +
                  'propositions_without_the_empty_clause.csv', 'rt') as fin:
                for vector in fin:
                    problem = PLSatProblemXML(vector)
                    problem.run_ttprover()
                    row += 1
                    fout.write(str(row)+','+problem.sat+'\n')

    # write another  version of data for ML
    # the vector of selected clauses + satisfiability
    if version == 2:
        with open('./data/'+str(no_prop)+'_prop_version2_xml.cvs', 'wt') as fout:
            with open('./data/list_of_clause_sets_containing_2_' +
                  'propositions_without_the_empty_clause.csv', 'rt') as fin:
                for vector in fin:
                    problem = PLSatProblemXML(vector)
                    problem.run_ttprover()
                    fout.write(vector.strip()+','+problem.sat+'\n')

    # write the 3rd version of data for ML
    # complex vector + satisfiability
    # each element of the vector is a product of prime numbers
    # for example, p0 or ~p1:
    # p0 is 2, p1 is 3, ~p1 is 3x3, so p0 or ~p1 is equal to 2x3x3 = 18.
    if version == 3:
        with open('./data/'+str(no_prop)+'_prop_version3.cvs', 'wt') as fout:
            with open('./data/list_of_clause_sets_containing_2_' +
                  'propositions_without_the_empty_clause.csv', 'rt') as fin:
                for vector in fin:
                    #vector = fin.readline()
                    problem = PLSatProblem(vector)
                    problem.run_ctlrp()
                    fout.write(vector.strip()+','+problem.sat+'\n')

