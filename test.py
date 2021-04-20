import json
import os

f = open("data.json", "r+")
# print(f)
y = json.load(f)

print(y)
#word = input("Enter Word: ")

dict = {}

command = input("Input command: ")

string_list = command.split("|")

print(string_list)

dict.update({string_list[0]: string_list[1]})

print(dict)


# f.write(str({dict.keys()}) + ":" + str({dict.values()}))
# f.close()

y.update(dict)

# print(y)
if os.path.exists("data.json"):
    os.remove("data.json")

if "data.json":
    with open("data.json", "w") as f:
        json.dump(y, f)


f.close()
