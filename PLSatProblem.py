"""
Each instance of PLSatProblem represents a propositional logic satisfiability problem.
"""
import csv

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
        zero = 0
        pl_clause = 'or('
        for i, x in enumerate(clause):
            if x == '0':
                zero += 1
                continue
            elif x == '1':
                pl_clause += 'p'+str(i)+', '
            elif x == '2':
                pl_clause += 'not(p'+str(i)+'), '
            else:
                pass

        pl_clause = pl_clause.strip(', ')
        pl_clause += ')'

        if zero == len(clause):# all are zeros
            return 'F' #The empty clause
        elif len(clause)-zero == 1:# single proposition
            pl_clause = pl_clause.replace('or(', '')# remove 'or(' and ')'
            return pl_clause[0:len(pl_clause)-1]
        else:
            return pl_clause


    def create_ctlrp_input_body(self):
        num_zeros = self.select_clauses.count('0')
        len = 3**PLSatProblem.num_propositions-1 # no empty clause

        body = ''
        for i, s in enumerate(self.select_clauses.split(',')):
            #print('--'+str(i)+','+s)
            if int(s) != 0:
                body += PLSatProblem.all_pl_clauses[i]+', '
        body = body.strip(', ') # remove the last comma and space

        if len-num_zeros == 1:# only one clause is selected, then double it because it is satisfiable anyway.
            body += ', '+body

        return body

    def create_ctlrp_input(self):
        problem = self.get_ctlrp_input_head()
        problem += self.create_ctlrp_input_body()
        problem += self.get_ctlrp_input_tail()
        return problem

    def check_satisfiability(self):
        self.sat = 'unsatisfiable'
        pass

    @classmethod
    def get_file_of_all_clauses(cls):
        return 'data/clauses_for_'+str(cls.num_propositions)+'_propositions.csv'




#main
if __name__ == '__main__':
    PLSatProblem.init_class_properties(2)

    """
    problem = PLSatProblem('1,0,0,0,0,0,0,0,0,1')
    for i, (c, pl) in enumerate(zip(problem.all_clauses, problem.all_pl_clauses), start=1):
        print(i, c, pl)
    """

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
