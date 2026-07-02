import json
# First we import json into python file


# with open("r1.json") as file:
#     data = json.load(file)

# 2nd we use the json dictionary load method to parse the "r1.json" file[string] listed into a python dictionary

# json.load is used to open and interpret a file
# json.loads is used when the file is already opened as a string and in RAM and needs to be converted into a python dictionary
# the following showcase json.loads which does not work in this version of VScode.


router_dict = {
  "router": {
    "hostname": [
      "Router1"
    ],
    "interfaces": [
      {
        "interface": [
          {
            "$": {
              "id": "0",
              "enabled": "true"
            },
            "name": [
              "GigabitEthernet0/0"
            ],
            "ip_address": [
              "192.168.1.3"
            ],
            "mask": [
              "255.255.255.0"
            ]
          },
          {
            "$": {
              "id": "1",
              "enabled": "true"
            },
            "name": [
              "GigabitEthernet0/1"
            ],
            "ip_address": [
              "172.16.2.1"
            ],
            "mask": [
              "255.255.255.0"
            ]
          },
          {
            "$": {
              "id": "2",
              "enabled": "true"
            },
            "name": [
              "GigabitEthernet0/2"
            ],
            "ip_address": [
              "10.0.0.1"
            ],
            "mask": [
              "255.0.0.0"
            ]
          }
        ]
      }
    ],
    "routes": [
      {
        "route": [
          {
            "destination": [
              "192.168.1.2"
            ],
            "mask": [
              "255.255.255.0"
            ],
            "gateway": [
              "201.1.113.4"
            ]
          },
          {
            "destination": [
              "0.0.0.0"
            ],
            "mask": [
              "0.0.0.0"
            ],
            "gateway": [
              "201.1.113.4"
            ]
          }
        ]
      }
    ]
  }
}

router_json =json.dumps(router_dict)

# Using dump: exports info to file
# Using dumps: Holds the json data in RAM
# Using load: imports file/loads the file 
# Using loads: to turn information into a string and Hold it in RAM


data = json.loads(router_json)


# print(data)

# # Solution:
# {'router': {'hostname': ['Router1'], 'interfaces': [{'interface': 
# [{'$': {'id': '0', 'enabled': 'true'}, 'name': ['GigabitEthernet0/0'], 'ip_address': ['192.168.1.3'], 'mask': ['255.255.255.0']}, 
# {'$': {'id': '1', 'enabled': 'true'}, 'name': ['GigabitEthernet0/1'], 'ip_address': ['172.16.2.1'], 'mask': ['255.255.255.0']}, 
# {'$': {'id': '2', 'enabled': 'true'}, 'name': ['GigabitEthernet0/2'], 'ip_address': ['10.0.0.1'], 'mask': ['255.0.0.0']}]}], 
# 'routes': [{'route': 
# [{'destination': ['192.168.1.2'], 'mask': ['255.255.255.0'], 'gateway': ['201.1.113.4']}, 
# {'destination': ['0.0.0.0'], 'mask': ['0.0.0.0'], 'gateway': ['201.1.113.4']}]}]}}

# print(data['router']['routes'])

# # Solution:
# [{'route': 
# [{'destination': ['192.168.1.2'], 'mask': ['255.255.255.0'], 'gateway': ['201.1.113.4']}, 
# {'destination': ['0.0.0.0'], 'mask': ['0.0.0.0'], 'gateway': ['201.1.113.4']}]}]

# print(router_json)
# print(router_dict)

# The following is an example it does not work in this example
# with open(data.json, 'w') as file:
#     json.dump(router_dict, file, indent=2)
