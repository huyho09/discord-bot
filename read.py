import json
import os

f = open("data.json", "r+")
# print(f)
y = json.load(f)

word = input("Enter Word: ")

for i, j in y.items():
    if word == i.lower():
        print(j)
