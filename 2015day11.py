import re
#"cqjxjnds"
password = "cqjxxyzz"
alphabet = "abcdefghijklmnopqrstuvqxyz"


alpha = list()
for i in password[::-1]:
    alpha.append(ord(i))

def addone(input, index):
    if len(input) <= index:
        input.append(97)
    else:
        input[index] += 1

    if input[index] >= 123:
        input[index] = 97
        addone(input, index + 1)
    return input

def checkseq(input):
    counter = 0
    for num in input[:len(input) - 2]:
        if num == input[counter + 1] + 1 and num == input[counter + 2] + 2:
            return True
        counter += 1
    return False

def checkiol(input):
    if 105 in input or 111 in input or 108 in input:
        return False
    return True

def checkdubs(input):
    dubstring = ""
    for i in input[:-1]:
        dubstring += chr(i)
    pattern = re.compile(r"(\w)\1")
    matches = pattern.findall(dubstring)
    if len(matches) >= 2:
        return True
    return False

#checkdubs([118, 113, 112, 120, 106, 113, 99])
#checkdubs([97, 97, 97, 104, 106, 106, 99])



def mainfunc(input):
    santapw = False
    seqflag = False
    iolflag = False
    dubsflag = False
    while True:
        input = addone(input, 0)
        seqflag = checkseq(input)
        iolflag = checkiol(input)
        dubsflag = checkdubs(input)
        if seqflag == True and iolflag == True and dubsflag == True:
            break
        else:
            seqflag = False
            iolflag = False
            dubsflag = False
    return input

final = mainfunc(alpha)


finalpw = ""
for i in final[::-1]:
    finalpw += chr(i)

print(finalpw)