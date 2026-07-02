import xmltodict

with open('r1.xml') as file:
    xml_data = file.read()

# this means to open the file listed and keep it open until xml_data = file.read() is finished [i.e. until file is read entirely and then it closes]

data = xmltodict.parse(xml_data)