import sys
import os
import xml.etree.ElementTree as ET
from itertools import product
import logging

class TruthTableProver:
    OPERATORS = ('and', 'or', 'not', 'imp')

    def __init__(self, input_file=None, input_string=None):

        #logging.basicConfig(level=logging.DEBUG, format='%(message)s')
        #logging.basicConfig(level=logging.INFO, format='%(message)s')
        logging.basicConfig(level=logging.WARNING, format='%(message)s')

        if input_file != None:
            tree = ET.parse(input_file)
            self.root = tree.getroot()
        else:
            self.root = ET.fromstring(input_string)

        self.pset = self.set_prop(self.root)
        self.plist = list(self.pset)


    def print_formula(self, node):
        str = ''
        #logging.debug('current node:', node.tag, len(node))
        if (len(node) != 0):
            str += node.tag + '('
            for child in node:
                str += self.print_formula(child)
                str += ', '
            str = str[0:-2]
            str += ')'
        else:
            str += node.tag
        return str


    def set_prop(self, root):
        list_prop = list()
        stack = [root]
        while len(stack) != 0:
            node = stack.pop()
            if node.tag not in TruthTableProver.OPERATORS:
                list_prop.append(node.tag)
            else:
                for child in node:
                    stack.append(child)
        return set(list_prop)

    def assign_props(self, temp_root, bools):
        result = ''
        for i, prop in enumerate(self.plist):
            result += prop + '=' + bools[i] + '; '
            for node in temp_root.iter(self.plist[i]):
                node.tag = bools[i]
        return result

    def cal_and(self, node):
        result = 'true';
        for child in node:
            if child.tag == 'false':
                result = 'false'
                break
        node.tag = result


    def cal_or(self, node):
        result = 'false';
        for child in node:
            if child.tag == 'true':
                result = 'true'
                break
        node.tag = result


    def cal_imp(self, node):
        result = 'true';
        if node[0].tag == 'true' and node[1].tag == 'false':
            result = 'false'
        node.tag = result


    def cal_not(self, node):
        if node[0].tag == 'true':
            node.tag = 'false'
        else:
            node.tag = 'true'

    def prove(self, node):
        if node.tag == 'true' or node.tag == 'false':
            return
        for child in node:
            if child.tag in TruthTableProver.OPERATORS:
                self.prove(child)
        if node.tag == 'and':
            self.cal_and(node)
        elif node.tag == 'or':
            self.cal_or(node)
        elif node.tag == 'imp':
            self.cal_imp(node)
        elif node.tag == 'not':
            self.cal_not(node)

    def run(self, test_satisfiability=True, test_validity=False):
        logging.info("Input:\n" + ET.tostring(self.root, encoding='unicode'))
        logging.info("The set of all propositions is " + str(self.pset))

        count = 0
        final_result = set()
        for item in product(('true', 'false'), repeat=len(self.pset)):
            # copy the tree. Each time temp_tree will be changed.
            temp_root = ET.fromstring(ET.tostring(self.root, encoding='unicode'))
            logging.info(str(count) + '. ' + self.assign_props(temp_root, item))
            count += 1
            #print(ET.tostring(temp_root, encoding='unicode'))
            logging.info(self.print_formula(temp_root))

            self.prove(temp_root)

            logging.debug(ET.tostring(temp_root, encoding='unicode'))
            logging.info(self.print_formula(temp_root))
            logging.info('result: ' + temp_root.tag + '\n')
            final_result = final_result | {temp_root.tag}

        if test_satisfiability:
            if 'true' not in final_result:
                logging.info('========\nfinal result: unsatisfiable\n\n')
                return 'unsat'
            else:
                logging.info('========\nfinal result: satisfiable\n\n')
                return 'sat'

        if test_validity:
            if 'false' not in final_result:
                logging.info('========\nfinal result: valid\n\n')
                return 'valid'
            else:
                logging.info('========\nfinal result: not valid\n\n')
                return 'not valid'



#### Main
if __name__ == '__main__':
    if len(sys.argv) != 2:
        logging.warning('Wrong arguments')
        sys.exit(0)
    elif not os.path.isfile(sys.argv[1]):
        logging.warning('File does not exist.')
        sys.exit(0)
    else:
        input_file = sys.argv[1]

    #prover = TruthTableProver(input_file)
    #logging.info(prover.run(test_satisfiability=True))

    prover = TruthTableProver(input_string='<and><p0/><not><p0/></not></and>')
    logging.info(prover.run(test_satisfiability=True))

