

input_stream = open("2015day5.txt", "r")

nice_counter = 0
vowel_counter = 0
double_letters = False

for line in input_stream.readlines():
    double_letters = False
    vowel_counter = 0
    if 'ab' in line:
        continue
    elif 'cd' in line:
        continue
    elif 'pq' in line:
        continue
    elif 'xy' in line:
        continue
    else:
        lholder = ""
        for i in line:
            if lholder == i:
                double_letters = True
            lholder = i
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                vowel_counter += 1
        if double_letters is True and vowel_counter >= 3:
            nice_counter += 1


print(nice_counter)

input_stream.close()

########################################################################################################################
########################################################################################################################
#part2


input_stream = open("2015day5.txt", "r")


previous_letter = ""
previous_previous_letter = ""
letter_pair = ("", "")

nice_counter = 0

character_counter = 0
for readline in input_stream.readlines():

    cond1flag = False
    cond2flag = False

    previous_previous_letter = ""
    previous_letter = ""

    count = 0
    for i in readline:
        if cond1flag and cond2flag:
            break
        autonice = i * 4
        if autonice in readline:
            cond1flag = True
            cond2flag = True
            break
        if not cond1flag or not cond2flag:
            if previous_previous_letter == i and previous_previous_letter != "":
                cond2flag = True
            if previous_letter != "" and i != "" and i != "\n":
                comb = previous_letter + i
                if readline.count(comb) > 1:
                    first = readline.find(comb, 0)
                    second = readline.find(comb, readline.index(comb) + 1)
                    if first + 1 < second:
                        #print(str(readline.count(comb)))
                        cond1flag = True
        previous_previous_letter = previous_letter
        previous_letter = i
        count += 1
    character_counter = 0
    if character_counter == 4:
        print(character_counter)
    # print(cond1flag)
    # print(cond2flag)
    if cond1flag and cond2flag:
        nice_counter += 1

print(str(nice_counter))

input_stream.close()

naughty = 0

with open('2015day5.txt', 'r') as f:
    strings = f.read().split()
f.close()

import regex
naughty = 0
for s in strings:
    if regex.match(r"\w*(\w\w)\w*\1\w*", s) is None:
        naughty += 1
    elif regex.match(r"\w*(\w)[^\1]\1\w*", s) is None:
        naughty += 1

print(len(strings) - naughty)

