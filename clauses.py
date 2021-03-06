#!/usr/bin/python3
# Generate all possible clauses
import sys

from pprint import pprint
import itertools


def generate_all_possible_clauses(num_of_prop=2):
    """
    format:
    p1's value,p2's value
    0,0 => empty clause
    1,2 => p1 v ~p2
    return an object of itertools.product
    """
    # return itertools.product(range(-1, 2), repeat=num_of_prop)
    return itertools.product(range(0, 3), repeat=num_of_prop)


def generate_all_possible_clauses_old(num_of_variables=2):
    """
    Deprecated
    format:
    number,p1's value,p2's value
    1,0,0 => 1, empty clause
    2,1,-1 => 2, p1 v ~p2
    """
    if num_of_variables > 10:
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
    """
    Deprecated
    :param clauses:
    :return:
    """
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
    with open('data/clauses_for_' + str(num) + '_propositions.csv', 'wt') as fout:
        csvout = csv.writer(fout)
        csvout.writerows(clauses)


def write_clauses_tofile(clauses: itertools.product, num):
    import csv
    with open('data/clauses_for_' + str(num) + '_propositions.csv', 'wt') as fout:
        csvout = csv.writer(fout)
        csvout.writerows(clauses)


def verify_arg(arg):
    """
    Verify the argument, which indicates the number of the propositions involved. The number has to be in [2, 10]
    :param arg: the number of propositions, which a user inputs
    :return: the tuple, whose first element is a boolean indicating whether args is valid or not and
    whose second element is the number of propositions or error code.
    """
    valid = True
    num = 0
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
if __name__ == '__main__':
    result = verify_arg(sys.argv)
    np = 0
    if not result[0]:
        print('The argument is wrong. The argument is an integer between 2 and 10, inclusively')
        print('Example: python3 clause.py 2')
        sys.exit(0)
    else:
        np = result[1]
    clauses = generate_all_possible_clauses(np)
    write_clauses_tofile(clauses, np)
