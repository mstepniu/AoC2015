import re
with open("2015day8.txt") as input_stream:
    alldata = [line.rstrip('\n') for line in input_stream]

literals = list()
bigcount = 0

for line in alldata:
    bigcount += len(line)
    newline = line.strip("\"")

    if "\\\\" in newline:
        newline = newline.replace("\\\\", "1")
    if "\\\"" in newline:
        newline = newline.replace("\\\"", "1")
    #
    # if "\\x" in newline:
    #     newline = newline.replace("\\x", "")

    result = re.sub(r"\\x\w\w","1", newline)

    if result:
        literals.append(result)
        #print("Results: " + result)
    else:
        literals.append(newline)
        #print("Newline: " + newline)
    #print(line)

counter = 0
for _ in literals:
    counter += len(_)

finalpart1 = bigcount - counter
print(finalpart1)


crapcounter = 0
for line in alldata:
    crapcounter += 2
    for x in line:
        if x == "\"":
            crapcounter += 2
        elif x == "\\":
            crapcounter += 2
        else:
            crapcounter += 1

finalpart2 = crapcounter - bigcount
print(finalpart2)

