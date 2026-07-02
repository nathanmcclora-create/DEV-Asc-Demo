import xmltodict

from pathlib import Path # Added this line to resolve issue because of version being used

file_path = Path(__file__).parent / "r1.xml" # Added this line to resolve issue because of version being used

with open(file_path) as file:
    xml_data = file.read()

# this means to open the file listed and keep it open until xml_data = file.read() is finished [i.e. until file is read entirely and then it closes]
# had to google a solution to this because they way the professor does the example --- it doesn't work for the version I'm using


data = xmltodict.parse(xml_data)

print(data["router"]["interfaces"])

# Solution:
# {'interface': [{'@id': '0', '@enabled': 'true', 'name': 'GigabitEthernet0/0', 'ip_address': '192.168.1.3', 'mask': '255.255.255.0'}, 
# {'@id': '1', '@enabled': 'true', 'name': 'GigabitEthernet0/1', 'ip_address': '172.16.2.1', 'mask': '255.255.255.0'}, 
# {'@id': '2', '@enabled': 'true', 'name': 'GigabitEthernet0/2', 'ip_address': '10.0.0.1', 'mask': '255.0.0.0'}]}