import re

puzzle_input = "1113222113"
test_input = "21"

numbs = list()

lastchar = ""


#numbs is the list of all numbers
#samelist is a list of duplicates that gets cleared

samelist = list()
newstring = test_input
#brute forcing doesn't work for range 50 - takes too long
for z in range(1):
    numbs.clear()
    for i in newstring:
        numbs.append(i)
    numbs.append("x")
    newstring = ""
    for x in range(len(numbs) - 1):
        if numbs[x] == numbs[x+1]:
            samelist.append(numbs[x])
        else:
            samelist.append(numbs[x])
            if len(samelist) == 1:
                newstring += "1" + numbs[x]
            elif len(samelist) == 2:
                newstring += "2" + numbs[x]
            elif len(samelist) == 3:
                newstring += "3" + numbs[x]
            elif len(samelist) == 4:
                newstring += "4" + numbs[x]
            elif len(samelist) == 5:
                newstring += "5" + numbs[x]
            elif len(samelist) == 6:
                newstring += "6" + numbs[x]
            elif len(samelist) == 7:
                newstring += "7" + numbs[x]
            elif len(samelist) == 8:
                newstring += "8" + numbs[x]
            elif len(samelist) == 9:
                newstring += "9" + numbs[x]
            samelist.clear()


from itertools import groupby
def look_and_say2(input):
    return ''.join(str(len([1 for _ in v])) + k for k, v in groupby(input))

#p = "1113222113"
p = "21"
for _ in range(1):
    p = look_and_say2(p)

def test1(input):
    count = 0
    for k, v in groupby(input):
        for _ in v:
            count += 1
            count += len(k)
            input_string = ''.join(str(len([_])) + k)
    print(count)
    return input_string
        # for _ in v:
        #     strtest = strtest + str(len(list(v))) + str(k)

def test2(input_string, num_iterations):
    for i in range(num_iterations):
        input_string = ''.join([str(len(list(g))) + str(k) for k, g in groupby(input_string)])
    return input_string


strwhat = test1("21")
print("Test1: " + str(len(strwhat)))
print("Test2: " + str(len(test2(("21"), 1))))
#print("q is: " + q)

print("Part1: " + str(len(newstring)))
print("Part2: " + str(len(p)))