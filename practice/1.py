import json

num = [2, 3, 4, 5, 6]
filename = 'num.json'
with open(filename, 'w') as f:
    json.dump(num, f)

assert 1+3 < 9