#!/usr/local/bin/python3.7
# Generate all possible clauses

from pprint import pprint

def generate_all_possible_clauses(num_of_variables=2):
  """ format:
  number,p1's value,p2's value
  1,0,0 => 1, empty clause
  2,1,-1 => 2, p1 v ~p2
  """
  if (num_of_variables>10):
    print("Error: Too many propositions. "+
    "The number of propositions should be less than or equal to 10")
    return

  clauses = list()
  for i in range(0, num_of_variables):
    clauses = add_another_variable(clauses)
  for i in range(0, len(clauses)):
    clauses[i].insert(0, i) #insert line number
  write_clauses(clauses, num_of_variables)

def add_another_variable(clauses:list) -> list:
  three = [0, 1, -1]
  new_list = list()
  if len(clauses) == 0:
    new_list = [[0], [1], [-1]]
    return new_list
  for c in clauses:
    for i in range(0, 3):
      one = list()
      one.extend(c)
      one.append(three[i])
      new_list.append(one)
      #pprint(c)
  return new_list

def write_clauses(clauses: list, num):
  import csv
  with open('data/table_of_clauses_for_'+str(num)+'_propositoins.csv', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(clauses)

"""
for i in range(-1,2):
  print('Hello World %d', i)
"""

"""
count = 1;
for m in ['0', '1', '-1']:
  for n in ['0', '1', '-1']:
    #print('%d,%s,%s' % (count, m, n))
    print('{},{},{}'.format(count, m, n))
    count+=1
tmp = list()
tmp = add_another_variable(tmp);
pprint(tmp)
tmp = add_another_variable(tmp);
pprint(tmp)
"""

"""
import sys
generate_all_possible_clauses(int(sys.argv[1]));
"""

#main
generate_all_possible_clauses(2);
