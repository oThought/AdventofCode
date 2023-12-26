f = open("Data.txt", "r")
data = f.readlines()

def checkstring(string, number):
    positions = []
    start = 0
    while True:
        start = string.find(number, start)
        if start == -1:
            break
        positions.append(start)
        start += 1
    return positions


def checklineSTR(line):
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    output = []
    for number in numbers:
        if number in line:
            positions = checkstring(line, number)
            for position in positions:
                output.append(int(f"{position}{numbers.index(number)}")+11)
    return output

def checklineINT(line):
    positions = []
    for x in range(len(line)):
        if line[x].isdigit() == True:
            positions.append(int(f"{x}{line[x]}")+10)
    return positions

def findextremes(list):
    lowest = 10000
    highest = 0
    for num in list:
        if num < lowest:
            lowest = num
        if num > highest:
            highest = num
    return str(lowest), str(highest)

final = 0
for line in data:
    strings = checklineSTR(line)
    integers = checklineINT(line)
    allnums = strings + integers
    lowest, highest = findextremes(allnums)
    combined = int(f"{lowest[-1]}{highest[-1]}")
    final += combined

print(final)