
#(999, 999)

lights = dict()

for i in range(1000):
    for j in range(1000):
        lights[(i, j)] = 0



input_stream = open("2015day6.txt", "r")

for line in input_stream:
    if "on" in line:
        turnon = line.split()
        first = turnon[2]
        ffc, fsc = first.split(',')
        second = turnon[4]
        sfc, ssc = second.split(',')
        for x in range(int(ffc), int(sfc) + 1):
            for y in range(int(fsc), int(ssc) + 1):
                # change "+=" to "=" for part1
                lights[(x, y)] = lights[(x, y)] + 1

    elif "off" in line:
        turnon = line.split()
        first = turnon[2]
        ffc, fsc = first.split(',')
        second = turnon[4]
        sfc, ssc = second.split(',')

        for x in range(int(ffc), int(sfc) + 1):
            for y in range(int(fsc), int(ssc) + 1):
                # change "-=" to "= 0" and remove != check for part1
                if lights[(x ,y)] != 0:
                    lights[(x, y)] -= 1
    else:
        turnon = line.split()
        first = turnon[1]
        ffc, fsc = first.split(',')
        second = turnon[3]
        sfc, ssc = second.split(',')

        for x in range(int(ffc), int(sfc) + 1):
            for y in range(int(fsc), int(ssc) + 1):
                # part1 toggled off and on instead
                lights[(x, y)] += 2
from collections import Counter

lightson = 0
for key, value in lights.items():
    if value != 0:
        lightson += value

print(lightson)
input_stream.close()