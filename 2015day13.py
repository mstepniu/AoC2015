# https://adventofcode.com/2015/day/13

from itertools import product
from collections import defaultdict
with open("2015day13.txt") as input_stream:
    data = [line.rstrip('\n') for line in input_stream]

happiness = defaultdict(int)


people = list()

for i in data:

    pdata = i.rstrip(".").split()

    if pdata[2] == "gain":
        happiness[pdata[0] + pdata[10]] = int(pdata[3])
    else:
        happiness[pdata[0] + pdata[10]] = int("-" + pdata[3])
    if pdata[10] not in people:
        people.append(pdata[10])
# taken from https://docs.python.org/3/library/itertools.html#itertools.permutations
def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)
temp = permutations(people)

total = list()

totalc = 0

for i in temp:

    totalc = happiness[i[0] + i[1]] + happiness[i[1] + i[2]] + \
             happiness[i[2] + i[3]] + happiness[i[3] + i[4]] + \
             happiness[i[4] + i[5]] + happiness[i[5] + i[6]] + \
             happiness[i[6] + i[7]] + happiness[i[7] + i[0]] + \
             happiness[i[1] + i[0]] + happiness[i[2] + i[1]] + \
             happiness[i[3] + i[2]] + happiness[i[4] + i[3]] + \
             happiness[i[5] + i[4]] + happiness[i[6] + i[5]] + \
             happiness[i[7] + i[6]] + happiness[i[0] + i[7]]
    total.append(totalc)
    totalc = 0

print(max(total))


# 527 - too low
# 1059 - too high
# 1039 - too high
# 541 - wrong


# part2

people.append("Mark")
temp = permutations(people)

total.clear()
totalc = 0

# BRUTE FORCE not optimized
for i in temp:
    totalc = happiness[i[0] + i[1]] + happiness[i[1] + i[2]] + \
             happiness[i[2] + i[3]] + happiness[i[3] + i[4]] + \
             happiness[i[4] + i[5]] + happiness[i[5] + i[6]] + \
             happiness[i[6] + i[7]] + happiness[i[7] + i[8]] + \
             happiness[i[8] + i[0]] + happiness[i[0] + i[8]] + \
             happiness[i[8] + i[7]] + happiness[i[7] + i[6]] + \
             happiness[i[6] + i[5]] + happiness[i[5] + i[4]] + \
             happiness[i[4] + i[3]] + happiness[i[3] + i[2]] + \
             happiness[i[2] + i[1]] + happiness[i[1] + i[0]]


    total.append(totalc)
    totalc = 0

print(max(total))

# 733 - too high