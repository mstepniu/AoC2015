def isnum(input):
    if input.isnumeric():
        return True
    else:
        return False

linecounter = 0
missed = 0

with open("2015day7.txt") as input_stream:
    alldata = [line.rstrip('\n') for line in input_stream]

finalvalues = dict()

stopflag = False

findopp = "-> a"
testa = 0
dataoperations = list()

# for text in alldata:
#     if findopp in text:
#         if len(text) - text.index(findopp) == len(findopp):
#             print(text)

# while testa == 0 and stopflag == False:
#     if findopp.isnumeric():
#         stopflag = True
#         print(findopp)

infloop = 0

while "a" not in finalvalues:
    infloop += 1
    if infloop == 400:
        print("Broke out of loop")
        break
    for line in alldata:
        test = line.split(" ")
        if test[1] == "->":
            if isnum(test[0]):

                #part2 check if b and overwrite value
                if test[2] == "b":
                    finalvalues[test[2]] = "46065"
                else:
                    finalvalues[test[2]] = test[0]
            if test[0] in finalvalues:
                finalvalues[test[2]] = finalvalues[test[0]]
        elif test[1] == "LSHIFT":
            if test[0] in finalvalues:
                finalvalues[test[4]] = int(finalvalues[test[0]]) << int(test[2])
            linecounter += 1
        elif test[1] == "RSHIFT":
            if test[0] in finalvalues:
                finalvalues[test[4]] = int(finalvalues[test[0]]) >> int(test[2])
            linecounter += 1
        elif test[1] == "AND":
            if isnum(test[0]) and test[2] in finalvalues:
                finalvalues[test[4]] = int(test[0]) & int(finalvalues[test[2]])
            elif test[0] in finalvalues and test[2] in finalvalues:
                finalvalues[test[4]] = int(finalvalues[test[0]]) & int(finalvalues[test[2]])
        elif test[1] == "OR":
            if test[0] in finalvalues and test[2] in finalvalues:
                finalvalues[test[4]] = int(finalvalues[test[0]]) | int(finalvalues[test[2]])
        elif test[0] == "NOT":
            if test[1] in finalvalues:
                finalvalues[test[3]] = ~int(finalvalues[test[1]])
        else:
            missed += 1

print("Value of a: " + str(finalvalues["a"]))
