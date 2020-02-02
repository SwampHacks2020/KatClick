import json
import os
import shutil

with open('cat.json', 'r', encoding="utf-8") as data_file:
    data = json.load(data_file)

array = []
count = 473
bad = 84
index = 0
i = 0

for point in data['GraphImages']:
    if len(point) > 0:
        tempArr = ["pic" + str(count) + ".jpg"]
        for i in point:
            if i == "edge_liked_by" or i == "edge_media_to_comment":
                temp = point[i]['count']
            else:
                temp = point[i]
            tempArr.append(temp)
        if point["followers"] < 50:
            try:
                os.rename("C:/Code/PyCharm/KatClick/cat/" + "pic" + str(count) + ".jpg",
                          "C:/Code/PyCharm/KatClick/data/" + "BAD" + str(bad) + ".jpg")
            except FileNotFoundError:
                print("Wrong file or file path")
            tempArr[0] = "BAD" + str(bad) + ".jpg"
            bad += 1
        else:
            try:
                os.rename("C:/Code/PyCharm/KatClick/cat/" + "pic" + str(count) + ".jpg",
                          "C:/Code/PyCharm/KatClick/data/" + "pic" + str(count) + "_ADDED.jpg")
            except FileNotFoundError:
                print("Wrong file or file path")
        array.append(tempArr)
        count += 1

print(array)

with open('clean.json', 'w') as data_file:
    json.dump(array, data_file)



