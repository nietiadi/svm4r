"""
Each instance of PLSatProblem represents a propositional logic satisfiability problem.
"""
class PLSatProblem:


    def __init__(self, num_propositions, selected_clauses):
        """
        Constructor
        :param total_num_of_props: the total number of propositions in this problem
        :param set: a set of clauses
        """
        self.num_propositions = num_propositions
        self.select_clauses = selected_clauses
        self.all_clauses = self.load_all_clauses()#should be a class variable

    def get_ctl_input_head(self):
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

    def get_ctl_input_tail():
        """
        :return: the head of ctl-rp input file
        """
        tail = """
    ).
    end_of_list.
    end_problem.
        """
        return tail


    def load_all_clauses(self):
        return list();
    #HERE

    def create_ctl_input_body(self):
        pass

    def create_ctl_input(self):
        pass

    def check_satisfiability(self):
        self.sat = 'unsatisfiable'
        pass




# main
if __name__ == '__main__':
    problem = PLSatProblem(2, '1,0,0,0,0,0,0,0,0,1')

