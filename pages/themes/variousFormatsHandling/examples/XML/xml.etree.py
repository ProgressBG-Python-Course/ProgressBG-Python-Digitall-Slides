import xml.etree.ElementTree as ET  
tree = ET.parse('sample_data.xml')  
root = tree.getroot()


# print items attributes
print('\nAll attributes:')  
for elem in root:  
    for subelem in elem:
        print(subelem.attrib)


# print items data
print('\nAll item data:')  
for elem in root:  
    for subelem in elem:
        print(subelem.text)