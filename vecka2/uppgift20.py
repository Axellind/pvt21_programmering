import json

with open('massadata.json') as f:
    data = json.load(f)

total = 0
for i in data['entries']:
    total += float(i['total'])

total_value = sum(float(i['total']) for i in data['entries'])

print('total: ', total)
print('test: ', total_value)
  