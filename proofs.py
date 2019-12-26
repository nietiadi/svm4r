#!/usr/bin/python3
# Generate all possible combinations of clauses
import itertools
import csv


def get_proofs(num_of_propositions=2, include_empty_clause=False):
    """
   the csv file consisting of all combinations of different clauses
    eg. 0 on the first column means the first clause in clauses_for_x_propositions.csv is not selected.
    eg. 1 on the second column means the first clause in clauses_for_x_propositions.csv is selected.
    """
    if include_empty_clause:
        num_of_clauses = 3 ** num_of_propositions;
        fname = 'data/proofs_for_' + \
                str(num_of_propositions) + '_propositoins.csv'
    else:
        num_of_clauses = 3 ** num_of_propositions - 1;
        fname = 'data/proofs_not_include_empty_for_' + \
                str(num_of_propositions) + '_propositoins.csv'

    proofs = itertools.product(range(0, 2), repeat=num_of_clauses)

    with open(fname, 'wt') as fout:
        csvout = csv.writer(fout)
        csvout.writerows(proofs)


# with line numbers in the file. In the new version, the line numbers are removed
def get_proofs_old(num_of_propositions=2, include_empty_clause=False):
    """
    create the csv file consisting of all combinations of different clauses
    """
    if include_empty_clause:
        num_of_clauses = 3 ** num_of_propositions;
        fname = 'data/proofs_clause_for_' + \
                str(num_of_propositions) + '_propositoins.csv'
    else:
        num_of_clauses = 3 ** num_of_propositions - 1;
        fname = 'data/proofs_not_include_empty_clause_for_' + \
                str(num_of_propositions) + '_propositoins.csv'
    # print(length)
    rows = list()
    y = 0
    for x in itertools.product(range(0, 2), repeat=num_of_clauses):
        # print(y, x)
        one_row = list(x);
        one_row.insert(0, y);
        rows.append(one_row);
        y += 1

    # print(rows)
    with open(fname, 'wt') as fout:
        csvout = csv.writer(fout)
        csvout.writerows(rows)


# main
if __name__ == '__main__':
    # get_proofs(2, False);
    get_proofs(2, True);
