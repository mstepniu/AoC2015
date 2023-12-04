import re

with open("2015day12.txt", "r") as input_stream:
    input = input_stream.readlines()

strinput = input[0]

count = 0

pattern = re.compile(r"(-?[0-9]+)")
matches = pattern.finditer(strinput)
for match in matches:
    count += int(match.group(1))

print(count)
input_stream.close()
#part needs to use JSON to filter red fields
import json

def checkred(data: any) -> int:
    if type(data) == int:
        return data
    elif type(data) == list:
        print(data)
        return sum([checkred(d) for d in data])
    elif type(data) == dict and 'red' not in data.values():
        return checkred(list(data.values()))
    return 0


with open("2015day12.txt", "r") as file:
    data = json.load(file)

print(checkred(data))

file.close()

# inputJSON = json.dumps(data, indent=4)
# print(inputJSON)