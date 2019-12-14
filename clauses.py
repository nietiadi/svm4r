#!/usr/bin/python3
# Generate all possible clauses
import sys

from pprint import pprint


def generate_all_possible_clauses(num_of_variables=2):
    """ format:
    number,p1's value,p2's value
    1,0,0 => 1, empty clause
    2,1,-1 => 2, p1 v ~p2
    """
    if (num_of_variables > 10):
        print("Error: Too many propositions. " +
              "The number of propositions should be less than or equal to 10")
        return

    clauses = list()
    for i in range(0, num_of_variables):
        clauses = add_another_variable(clauses)
    for i in range(0, len(clauses)):
        clauses[i].insert(0, i)  # insert line number
    write_clauses(clauses, num_of_variables)


def add_another_variable(clauses: list) -> list:
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
            # pprint(c)
    return new_list


def write_clauses(clauses: list, num):
    import csv
    with open('data/clauses_for_' + str(num) + '_propositoins.csv', 'wt') as fout:
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


def verify_arg(arg):
    """
    Verify the argument, which indicates the number of the propositions involved. The number has to be in [2, 10]
    :param arg: the number of propositions, which a user inputs
    :return: the valid number of propositions
    """
    valid = True
    num = 0
    result = None
    if len(arg) != 2:
        valid = False
        return valid, -1
    else:
        str = arg[1]
        if not str.isdigit():
            valid = False
            return valid, -2
        else:
            num = int(str)
            if not (2 <= num <= 10):
                valid = False
                return valid, -3
    return valid, num



# main
if __name__=='__main__':
    result = verify_arg(sys.argv)
    np = 0
    if not result[0]:
        print('The argument is wrong. The argument is an integer between 2 and 10, inclusively')
        print('Example: python3 clause.py 2')
        sys.exit(0)
    else:
        np = result[1]
# generate_all_possible_clauses(2);
