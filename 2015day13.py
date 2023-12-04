

with open("2015day13.txt") as input_stream:
    data = [line.rstrip('\n') for line in input_stream]

happiness = dict()

#name at 0
#gain/lose at 2
#number at 3
#name at 10
for i in data:

    pdata = i.rstrip(".").split()

    if pdata[2] == "gain":
        happiness[pdata[0] + r"-" + pdata[10]] = pdata[3]
    else:
        happiness[pdata[0] + r"-" + pdata[10]] = "-" + pdata[3]

print(happiness)
