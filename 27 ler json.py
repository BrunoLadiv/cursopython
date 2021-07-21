import json

with open('jsonlist.txt', 'r') as file:
    jsonlist = file.read()
    jsonlist = json.loads(jsonlist)


for x,i in jsonlist.items():
    print(x)
    for k1, v1 in i.items():
            print(k1, v1)