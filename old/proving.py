#!/usr/bin/python3
"""
using ctl-rp to prove all proofs and give the answer, which is either 'sat' or 'unsat'

"""

import itertools
import csv

def proving(num_of_propositions=2, with_empty_clause=False):
  """
  create the csv file containing the results from ctl-rp
  """
  if with_empty_clause:
    fname = 'data/proofs_with_empty_clause_for_'+\
    str(num_of_propositions)+'_propositoins.csv'
  else:
    fname = 'data/proofs_without_empty_clause_for_'+\
    str(num_of_propositions)+'_propositoins.csv'
  
  fname = 'test.dat'
  with open(fname) as csvfile:
    csvin = csv.reader(csvfile)
    for row in csvin:
      #print(', '.join(row))
      print(row)



  """
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
  """


#main
proving(2, False);
#proving(2, True);
