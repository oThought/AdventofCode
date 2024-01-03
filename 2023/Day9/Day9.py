f = open("Data.txt", "r")
data = f.readlines()

def findDifference(numbers):
    output = []
    for number in range(len(numbers)):
        if number != 0:    
            output.append(int(numbers[number])-int(numbers[number-1]))
    return output
def checkZeroes(numbers):
    for number in numbers:
        if number != 0:
            return True
    return False

output = 0
for line in data:
    fulldata = []
    numbers = line.split()
    fulldata.append(numbers)
    new = findDifference(numbers)
    while checkZeroes(new):
        fulldata.append(new)
        new = findDifference(new)
    fulldata.append(new)
    next = []
    for f in fulldata:
        next.append(int(f[0]))
    for n in range(len(next)):
        if n != 0:
            x = next[::-1][n] - x
        else:
            x = 0
    output += x
        

print(output)