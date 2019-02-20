import json
with open('accountinfo.json', 'r') as f:
    f_dict=json.load(f)
    print(f_dict)
