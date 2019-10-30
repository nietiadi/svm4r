
import xml.etree.ElementTree as ET
OPERATORS = ('and', 'or', 'not', 'imp')

def set_prop(root):
    list_prop = list()
    stack = [root] 
    while len(stack)!=0:
        node = stack.pop()
        #print(node.tag+' ')
        if node.tag not in OPERATORS:
            list_prop.append(node.tag)
        else:
            for child in node:
                #stack.append(child) #BFS
                stack.insert(0, child)  # DFS
    return set(list_prop)


tree = ET.parse('camp.xml')
root = tree.getroot()
print(set_prop(root))