import json

with open('cat.json') as json_file:
    data = json.load(json_file)
    for p in data['GraphImages']:
        if p['is_video'] == true:
            delete p
