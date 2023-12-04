
#file is filled with '(' and ')'.  '(' means go up a floor.  ')' means go down a floor

day1 = open("2015day1.txt", "r", )


#find the final floor
for line in day1.readlines():
    print(line.count('(') - line.count(')'))


#find the first occurance of going to the basement (-1) ')' outnumber '(' by 1
floor = 0
index = 1
for _ in line:
    if _ == '(':
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print(index)
    index += 1

day1.close()