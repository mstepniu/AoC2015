from itertools import permutations

with open("2015day9.txt") as input_stream:
    alldata = [line.rstrip('\n') for line in input_stream]

cities = list()
linelist = list()
citydistance = dict()
for line in alldata:
    linelist = line.split()
    if linelist[0] not in cities:
        cities.append(linelist[0])
    if linelist[2] not in cities:
        cities.append(linelist[2])
    citydistance[linelist[0]+linelist[2]] = int(linelist[4])
    citydistance[linelist[2]+linelist[0]] = int(linelist[4])

linelist = list(permutations(cities, 8))

# change to shortest = 99999999 for part1
shortest = 0
for perm in linelist:
    currentdistance = citydistance[perm[0]+perm[1]] + citydistance[perm[1]+perm[2]] + citydistance[perm[2]+perm[3]] + \
        citydistance[perm[3]+perm[4]] + citydistance[perm[4]+perm[5]] + citydistance[perm[5]+perm[6]] + \
        citydistance[perm[6] + perm[7]]
    #change to currentdistance < shortest for part1
    if currentdistance > shortest:
        shortest = currentdistance

print(shortest)