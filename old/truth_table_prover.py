import xml.etree.ElementTree as et
from itertools import product
import sys
import os

# Replace by ttprover.py

OPERATORS = ('and', 'or', 'not', 'imp')
#BOOLS = ('false', 'true')

def print_formula(node):
    str=''
    #print('current node:', node.tag, len(node))
    if(len(node)!=0):
        str+=node.tag+'('
        for child in node:
            str+=print_formula(child)
            str+=', '
        str=str[0:-2]
        str+=')'
    else:
        str+=node.tag
    return str

def set_prop(root):
    list_prop = list()
    stack = [root] 
    while len(stack)!=0:
        node = stack.pop()
        if node.tag not in OPERATORS:
            list_prop.append(node.tag)
        else:
            for child in node:
                stack.append(child)
    return set(list_prop)

def assign_props(tree, plist, bools):
    i = 0
    result = ''
    for prop in plist:
        result+=prop+'='+bools[i]+'; '
        for node in tree.iter(plist[i]):
            node.tag = bools[i]
        i+=1
    return result

def cal_and(node):
    result = 'true';
    for child in node:
        if child.tag == 'false':
            result = 'false'
            break
    node.tag = result
    
def cal_or(node):
    result = 'false';
    for child in node:
        if child.tag == 'true':
            result = 'true'
            break
    node.tag = result
    
def cal_imp(node):
    result = 'true';
    if node[0].tag=='true' and node[1].tag=='false':
        result = 'false'
    node.tag = result
    
def cal_not(node):
    if node[0].tag=='true':
        node.tag = 'false'
    else:
        node.tag = 'true'

def proof(node):
    #print(print_formula(node))
    if node.tag=='true' or node.tag=='false':
        #reture
        return
    for child in node:
        if child.tag in OPERATORS:
            proof(child)
    if node.tag == 'and':
        cal_and(node)
    elif node.tag == 'or':
        cal_or(node)
    elif node.tag == 'imp':
        cal_imp(node)
    elif node.tag == 'not':
        cal_not(node)

def run(xml_string):
    """
    for PLSatProblemXML to use

    :param xml_string: e.g. <and><p0/><not><p0/></not></and>
    :return: e.g. unsatisfiable
    """
    root = et.fromstring(xml_string)

    #print("Input: " + print_formula(root))
    pset = set_prop(root)
    #print("The set of all propositions is " + str(pset))
    plist = list(pset)

    count = 0
    final_result = set()
    for item in product(('true', 'false'), repeat=len(pset)):
        root = et.fromstring(xml_string)
        print(str(count) + '. ' + assign_props(root, plist, item))
        count += 1
        print(print_formula(root))
        proof(root)
        print(print_formula(root))
        print('result: ' + root.tag + '\n')
        final_result = final_result | {root.tag}

    if len(final_result) == 2:
        #print('========\nfinal result: satisfiable\n\n')
        return 'sat'
    elif 'true' not in final_result:
        #print('========\nfinal result: unsatisfiable\n\n')
        return 'unsat'
    else:
        #print('========\nfinal result: valid\n\n')
        return 'sat'


#### Main
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Wrong arguments')
        sys.exit(0)
    elif not os.path.isfile(sys.argv[1]):
        print('File does not exist.')
        sys.exit(0)
    else:
        input_file = sys.argv[1]

    tree = et.ElementTree(file=input_file)
    root = tree.getroot()

    print("Input: " + print_formula(root))
    pset = set_prop(root)
    print("The set of all propositions is " + str(pset))
    plist = list(pset)

    count = 0
    final_result = set()
    for item in product(('true', 'false'), repeat=len(pset)):
        tree = et.ElementTree(file=input_file)
        root = tree.getroot()
        print(str(count) + '. ' + assign_props(tree, plist, item))
        count += 1
        print(print_formula(root))
        proof(root)
        print(print_formula(root))
        print('result: ' + root.tag + '\n')
        final_result = final_result | {root.tag}

    if len(final_result) == 2:
        print('========\nfinal result: satisfiable\n\n')
    elif 'true' not in final_result:
        print('========\nfinal result: unsatisfiable\n\n')
    else:
        print('========\nfinal result: valid\n\n')




