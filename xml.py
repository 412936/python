import xml.dom.minidom as minidom

xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute')

Value = []

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'Value':
                if child.firstChild.nodeType == 3:
                    Value.append(child.firstChild.data)

sredn = []
for i in Value:
    i = i.replace(',', '.')
    sredn.append(float(i))
print(sum(sredn) / len(sredn))