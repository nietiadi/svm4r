import xml.etree.ElementTree as ET

def print_formula(node):
    str=''
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

tree = ET.parse('camp.xml')
root = tree.getroot()
print(print_formula(root))
