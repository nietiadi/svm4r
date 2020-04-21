"""
Each instance of PLSatProblem represents a propositional logic satisfiability problem.
"""
class PLSatProblem:


    def __init__(self, total_num_of_props, set):
        """
        Constructor
        :param total_num_of_props: the total number of propositions in this problem
        :param set: a set of clauses
        """
        self.total_num_of_props = total_num_of_props
        self.set = set
        self.clause_list = self.load_clause_list()

    def get_ctl_input_head(self):
        return """
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
    def load_clause_list(self):
        return list();
    #HERE




# main
if __name__ == '__main__':
    problem = PLSatProblem(2, '1,0,0,0,0,0,0,0,0,1')

