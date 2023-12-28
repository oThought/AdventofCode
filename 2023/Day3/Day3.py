f = open("Datatwo.txt", "r")
data = f.readlines()

alldata = []
symbols = "/@=+-*$%"
for line in data:
    for character in range(len(line)):
        alldata.append([data.index(line), character, line[character]])

def findNumbers(line):
    positions = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
"21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
"41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60",
"61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80",
"81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100",
"101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "111", "112", "113", "114", "115", "116", "117", "118", "119", "120",
"121", "122", "123", "124", "125", "126", "127", "128", "129", "130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "140"]
    for character in range(len(line)):
        if line[character].isdigit() != True:
            positions[character] = "x"
    numbers = []
    latestpoint = -1
    for point in range(len(positions)):
        if positions[point] == "x" and positions[point-1].isdigit() == True:
            numbers.append(positions[latestpoint+1:point])
            latestpoint = point
        elif positions[point] == "x":
            latestpoint = point
    if latestpoint+1 != len(line):
        numbers.append(positions[latestpoint+1:])
    return numbers

def findSurroundings(line):
    numbers = findNumbers(line)
    surroundings = []
    for number in numbers:
        try:
            x = number[0]
            y = number[-1]
            number.insert(0, str(int(x)-1))
            number.append(str(int(y)+1))
            try:
                number.remove("-1")
            except ValueError:
                pass
            surroundings.append(number)
        except IndexError:
            pass
    return surroundings

def hasSymbols(line):
    for char in line:
        if not str(char).isalnum() and not str(char).isspace() and char != ".":
            return True
    return False


def findSymbols(row, data):
    total = 0
    numbers = findNumbers(data[row])
    surroundings = findSurroundings(data[row])
    combined = [[x, y] for x, y in zip(numbers, surroundings)]
    for number in range(len(combined)):
        try:
            row1 = data[row-1][int(surroundings[number][0]):int(surroundings[number][-1])+1]
        except IndexError:
            row1 = [0]
        try:
            row2 = data[row][int(surroundings[number][0]):int(surroundings[number][-1])+1]
        except IndexError:
            row2 = [0]
        try:
            row3 = data[row+1][int(surroundings[number][0]):int(surroundings[number][-1])+1]
        except IndexError:
            row3 = [0]
        if hasSymbols(row1) == False and hasSymbols(row2) == False and hasSymbols(row3) == False:
            parts = data[row][int(numbers[number][0]): int(numbers[number][-1])+1]
            part = int("".join(parts))
            total += part
    return total

total = 0
for line in range(len(data)):
    total -= findSymbols(line, data)

for line in data:
    numbers = findNumbers(line)
    if len(findNumbers(line)) != 0:
        for i in range(len(findNumbers(line))):
            try:
                parts = line[int(numbers[i][0]): int(numbers[i][-1])+1]
                part = int("".join(parts))
                total += int(part)
            except IndexError:
                pass
print(total)