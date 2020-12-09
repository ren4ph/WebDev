import json

r = open("data.json")

strh = json.load(r)
print(type(strh))
items = {'A0':None, 'A1':None, 'A2':None, 'A3':None, 'A4':None, 'A5':None, 'A6':None, 'A7':None, 'A8':None, 'A9':None, 'B0':None, 'B1':None, 'B2':None, 'B3':None}

for i in strh:
    print(i, type(i))
    items[str(i)] = i

print(items['A7'])
print(type(items))

r.close()
