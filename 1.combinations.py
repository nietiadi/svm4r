#!/usr/local/bin/python3.7
# Generate all possible combinations of clauses

def generate_all_possible_combinations(num_of_variables=2):
  """
  2 propositions: use 1, 2, ..., 8 clauses.
  clauses = list()
  for i in range(0, num_of_variables):
    clauses = add_another_variable(clauses)
  for i in range(0, len(clauses)):
    clauses[i].insert(0, i) #insert line number
  write_clauses(clauses, num_of_variables)
  """
  length = total_number_of_clauses(num_of_variables) # when it is 2, then return 8
HERE
  count = 0
  for i in range(1, length+1):
    count = clause_combination(length, i)
  #write_combinations(clauses, num_of_variables)
  print("end"+str(1))

def total_number_of_clauses(num_of_variables:int) -> int:
  return (3 ** num_of_variables)-1
  

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
  with open('table_of_clauses_for_'+str(num)+'_propositoins.csv', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(clauses)

#main
generate_all_possible_combinations(2);
