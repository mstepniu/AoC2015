import collections
#coordinates of houses visited in a list

from collections import defaultdict



santa_pos = (0, 0)

houses_dict = {santa_pos: 1}



input_stream = open("2015day3.txt", "r")
santas_journey = input_stream.readline()

for next_house in santas_journey:
    if next_house == '>':
        santa_pos = (santa_pos[0] + 1, santa_pos[1])
    elif next_house == 'v':
        santa_pos = (santa_pos[0], santa_pos[1] - 1)
    elif next_house == '<':
        santa_pos = (santa_pos[0] - 1, santa_pos[1])
    elif next_house == '^':
        santa_pos = (santa_pos[0], santa_pos[1] + 1)
    else:
        print("unknown input")

    if santa_pos in houses_dict:
        houses_dict[santa_pos] += 1
    else:
        houses_dict[santa_pos] = 1

print(len(houses_dict))

input_stream.close()
########################################################################################################################
########################################################################################################################
#part2 with robo santa

santa_pos = (0, 0)
robo_pos = (0, 0)

#init houses to 2 because both santa and robo are at the same house
houses_dict = {santa_pos: 2}
input_stream = open("2015day3.txt", "r")
santas_journey = input_stream.readline()

counter = 0
for next_house in santas_journey:
    counter += 1
    if counter % 2:
        if next_house == '>':
            robo_pos = (robo_pos[0] + 1, robo_pos[1])
        elif next_house == 'v':
            robo_pos = (robo_pos[0], robo_pos[1] - 1)
        elif next_house == '<':
            robo_pos = (robo_pos[0] - 1, robo_pos[1])
        elif next_house == '^':
            robo_pos = (robo_pos[0], robo_pos[1] + 1)
        else:
            print("unknown input")

        if robo_pos in houses_dict:
            houses_dict[robo_pos] += 1
        else:
            houses_dict[robo_pos] = 1
    else:
        if next_house == '>':
            santa_pos = (santa_pos[0] + 1, santa_pos[1])
        elif next_house == 'v':
            santa_pos = (santa_pos[0], santa_pos[1] - 1)
        elif next_house == '<':
            santa_pos = (santa_pos[0] - 1, santa_pos[1])
        elif next_house == '^':
            santa_pos = (santa_pos[0], santa_pos[1] + 1)
        else:
            print("unknown input")

        if santa_pos in houses_dict:
            houses_dict[santa_pos] += 1
        else:
            houses_dict[santa_pos] = 1

print(len(houses_dict))

input_stream.close()