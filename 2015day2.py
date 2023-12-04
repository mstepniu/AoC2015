


day2 = open("2015day2.txt", "r")

wrappingpaper = 0
totalribbon = 0
totalbow = 0

for package in day2.readlines():
    length, width, height = package.split('x')

    surfacearea = 2 * int(length) * int(width) + 2 * int(width) * int(height) + 2 * int(height) * int(length)

    smallestside = list()

    smallestside.append(int(length))
    smallestside.append(int(height))
    smallestside.append(int(width))

    smallestside.sort()
    wrappingpaper += surfacearea
    wrappingpaper += int(smallestside[0]) * int(smallestside[1])

    # part2
    totalribbon += smallestside[0] * 2 + smallestside[1] * 2 + smallestside[0] * smallestside[1] * smallestside[2]


print(wrappingpaper)

print(totalribbon)



day2.close()