#!/usr/bin/python3
# Generate all possible combinations of clauses
import itertools
import csv


def write_list_of_clause_sets_to_file(num_of_propositions=2, include_empty_clause=False):
    """
    the csv file consisting of all combinations of different clauses
    eg. 0 on the first column means the first clause in clauses_for_x_propositions.csv is not selected.
    eg. 1 on the second column means the first clause in clauses_for_x_propositions.csv is selected.
    """
    if include_empty_clause:
        num_of_clauses = 3 ** num_of_propositions;
        fname = 'data/list_of_clause_sets_containing_' + \
                str(num_of_propositions) + '_propositoins.csv'
    else:
        num_of_clauses = 3 ** num_of_propositions - 1;
        fname = 'data/list_of_clause_sets_containing_' + \
                str(num_of_propositions) + '_propositoins_without_the_empty_clause.csv'

    proofs = itertools.product(range(0, 2), repeat=num_of_clauses)

    next(proofs) # delete the first line, which are all zeors, for instance, 0,0,0,0

    with open(fname, 'wt') as fout:
        csvout = csv.writer(fout)
        csvout.writerows(proofs)



# main
if __name__ == '__main__':
    #write_list_of_clause_sets_to_file(2, True);
    write_list_of_clause_sets_to_file(2, False);
