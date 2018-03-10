import json

with open("MOCK_DATA.json") as json_data:
    data = json.load(json_data)

dictionary = dict()
for d in data:
    temp = { }
    temp['date'] = d['date']
    temp['clicks'] = d['clicks']

    if d['product'] in dictionary:
        dictionary[d['product']].append(temp)
    else:
        dictionary[d['product']] = [temp]

print(dictionary['Contreau'])
