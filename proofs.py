#!/usr/local/bin/python3.7
# Generate all possible combinations of clauses
import itertools
import csv

def get_proofs(num_of_propositions=2, with_empty_clause=False):
  """
  create the csv file consisting of all combinations of different clauses
  """
  if with_empty_clause:
    num_of_clauses = 3**num_of_propositions;
    fname = 'proofs_with_empty_clause_for_'+\
    str(num_of_propositions)+'_propositoins.csv'
  else:
    num_of_clauses = 3**num_of_propositions-1;
    fname = 'proofs_without_empty_clause_for_'+\
    str(num_of_propositions)+'_propositoins.csv'
  #print(length)
  rows = list()
  y = 0
  for x in itertools.product(range(0,2), repeat=num_of_clauses):
    #print(y, x)
    one_row = list(x);
    one_row.insert(0, y);
    rows.append(one_row);
    y+=1

  #print(rows)
  with open(fname, 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(rows)

#main
get_proofs(2, False);
get_proofs(2, True);
