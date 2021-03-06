"""
Each instance of PLSatProblem represents a propositional logic satisfiability problem.
"""
import csv
import os
import logging
from pl_sat_problem_xml import PLSatProblemXML

class PLSatProblem:

    num_propositions = 0
    all_clauses = None
    all_pl_clauses = None

    @classmethod
    def init_class_properties(cls, num_propositions):
        """
        call this before making any PLSatProblem instance
        :param num_propositions: the total number of propositions in this problem
        """
        cls.mylog = logging.getLogger('sat')
        cls.mylog.setLevel(logging.INFO)

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
        self.problem = self.create_ctlrp_input()
        self.sat = None

    def get_ctlrp_input_head(self):
        """
        :return: the head of ctl-rp input file
        """
        head = """
begin_problem(test2).
list_of_descriptions.
name({*01*}).
author({*Lan Zhang*}).
status(unknown).
description({*Test a  CNF propositional logic clauses set*}).
end_of_list.
list_of_ctlformulae(axioms).
and(
"""
        return head

    def get_ctlrp_input_tail(self):
        """
        :return: the head of ctl-rp input file
        """
        tail = """
).
end_of_list.
end_problem.
        """
        return tail

    def get_ctlrp_input_satisfiable(self):
        head_n_tail = """
begin_problem(test2).
list_of_descriptions.
name({*01*}).
author({*Lan Zhang*}).
status(unknown).
description({*Test a  CNF propositional logic clauses set*}).
end_of_list.
list_of_ctlformulae(axioms).
SINGLE_CLAUSE.
end_of_list.
end_problem.
        """
        return head_n_tail


    @classmethod
    def load_all_clauses(cls):
        with open(cls.get_file_of_all_clauses(), 'rt') as fin:
            #lines = [x.strip() for x in fin.readlines()]
            csvin = csv.reader(fin, delimiter=',')
            lines = [x for x in csvin]
        return lines


    @classmethod
    def load_all_pl_clauses(cls): # Can handld the empty clause
        clauses = [PLSatProblem.translate_matrix_into_clauses(x) \
                   for x in cls.all_clauses]
        return clauses

    @classmethod
    def translate_matrix_into_clauses(cls, clause):
        """
        :param clause: e.g. (1,2)
        :return: or(p0,not(p2))
        """
        zero = 0
        pl_clause = 'or('
        for i, x in enumerate(clause):
            if x == '0':
                zero += 1
                continue
            elif x == '1':
                pl_clause += 'p'+str(i)+','
            elif x == '2':
                pl_clause += 'not(p'+str(i)+'),'
            else:
                pass

        pl_clause = pl_clause.strip(',')
        pl_clause += ')'

        if zero == len(clause):# all are zeros
            return 'F' #The empty clause
        elif len(clause)-zero == 1:# single proposition
            pl_clause = pl_clause.replace('or(', '')# remove 'or(' and ')'
            return pl_clause[0:len(pl_clause)-1]
        else:
            return pl_clause

    def create_ctlrp_input_body(self):
        body = ''
        for i, s in enumerate(self.select_clauses.split(',')):
            if int(s) != 0:
                body += PLSatProblem.all_pl_clauses[i]+','
        body = body.strip(',') # remove the last comma and space
        return body

    def create_ctlrp_input_body_2(self):
        num_zeros = self.select_clauses.count('0')
        len = 3**PLSatProblem.num_propositions-1 # no empty clause

        body = ''
        for i, s in enumerate(self.select_clauses.split(',')):
            if int(s) != 0:
                body += PLSatProblem.all_pl_clauses[i]+', '
        body = body.strip(', ') # remove the last comma and space

        if len-num_zeros == 1:# only one clause is selected, then double it because it is satisfiable anyway.
            body += ', '+body

        return body

    def create_ctlrp_input(self):
        num_zeros = self.select_clauses.count('0')
        len = 3 ** PLSatProblem.num_propositions - 1  # no empty clause
        if len-num_zeros == 1:# only one clause is selected, \
            # then remove and().
            problem = self.get_ctlrp_input_satisfiable()
            problem = problem.replace('SINGLE_CLAUSE', self.create_ctlrp_input_body())
        else:
            problem = self.get_ctlrp_input_head()
            problem += self.create_ctlrp_input_body()
            problem += self.get_ctlrp_input_tail()
        return problem

    def check_satisfiability(self):
        self.sat = 'unsat'
        pass

    @classmethod
    def get_file_of_all_clauses(cls):
        return 'data/clauses_for_'+str(cls.num_propositions)+'_propositions.csv'

    def run_ctlrp(self):
        with open('z_ctlrp_input', 'w') as fout:
            fout.write(self.problem)
        with os.popen('./ctlrp21_sourceforge/ctlrp21_x86_64 z_ctlrp_input') as pipe:
            result = pipe.read()
        try:
            index = result.index('Unsatisfiable')
            if index>=0:
                self.sat = 'unsat'
        except ValueError:
            pass

        try:
            index = result.index('Satisfiable')
            if index>=0:
                self.sat = 'sat'
        except ValueError:
            pass

    @classmethod
    def write_result_version1(cls):
        # write the simple version of data for ML
        # row number + satisfiability
        row = 0
        with open('./data/' + str(cls.num_propositions) + '_prop_version1.cvs', 'wt') as fout:
            with open('./data/list_of_clause_sets_containing_2_' +
                      'propositions_without_the_empty_clause.csv', 'rt') as fin:
                for vector in fin:
                    problem = PLSatProblem(vector)
                    problem.run_ctlrp()
                    row += 1
                    fout.write(str(row) + ',' + problem.sat + '\n')


    @classmethod
    def write_result_version2(cls):
        # write another  version of data for ML
        # the vector of selected clauses + satisfiability
        with open('./data/' + str(cls.num_propositions) + '_prop_version2.cvs', 'wt') as fout:
            with open('./data/list_of_clause_sets_containing_2_' +
                      'propositions_without_the_empty_clause.csv', 'rt') as fin:
                for vector in fin:
                    problem = PLSatProblem(vector)
                    problem.run_ctlrp()
                    fout.write(vector.strip() + ',' + problem.sat + '\n')


    @classmethod
    def write_result_version3(cls):
        # write the 3rd version of data for ML
        # complex vector + satisfiability
        # each element of the vector is a product of prime numbers
        # for example, p0 or ~p1:
        # p0 is 2, p1 is 3, ~p1 is 3x3, so p0 or ~p1 is equal to 2x3x3 = 18.
        with open('./data/' + str(cls.num_propositions) + '_prop_version3.cvs', 'wt') as fout:
            with open('./data/list_of_clause_sets_containing_' + str(cls.num_propositions) +
                      '_propositions_without_the_empty_clause.csv', 'rt') as fin:
                for vector in fin:
                    problem = PLSatProblem(vector)
                    problem.run_ctlrp()
                    index = 0
                    new_vector = vector.split(',')

                    # get help from PLSatProblemXML
                    PLSatProblemXML.init_class_properties(cls.num_propositions)
                    for i, j in zip(new_vector, PLSatProblemXML.all_clauses_in_numbers):
                        new_vector[index] = str(int(i)*j)
                        index+=1
                    new_vector_str = str(new_vector)[1:-2]
                    new_vector_str = new_vector_str.replace('\'', '')
                    new_vector_str = new_vector_str.replace(' ', '')
                    logging.debug('v3: '+new_vector_str)
                    fout.write(new_vector_str + ',' + problem.sat + '\n')





if __name__ == '__main__':
    # Generate data
    no_prop = 2
    PLSatProblem.init_class_properties(no_prop)
    #PLSatProblem.write_result_version1()
    #PLSatProblem.write_result_version2()
    PLSatProblem.write_result_version3()






