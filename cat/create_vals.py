import json
import os
from os import path
from decimal import Decimal

with open('../data/all_cleaned.json', 'r', encoding="utf-8") as data_file:
    data = json.load(data_file)

engagements = []

for p in data:
    # print(p)
    if "BAD" in p[0]:
        engagements.append(-1)
    else:
        eng = p[1] / p[3]
        output = round(eng, 3)
        engagements.append(output)

j = 0
count = 0
var = len(engagements)
for j in range(0, var):
    name = "pic" + str(j) + "_ADDED_CROP.jpg"
    if not path.exists("../data/" + name):
        print(name)
        count+=1
        engagements[j] = -1

engagements[:] = (value for value in engagements if value != -1)
file = open("../data/cat_data.txt", "w")

# i = 0
for n in engagements:
    file.write(str(n) + "\n")
    # file.write(str(i) + " " + str(n) + "\n")
    # i += 1

file.close()


