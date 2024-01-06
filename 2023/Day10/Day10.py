f = open("Datatwo.txt", "r")
data = f.readlines()
complete = [[] for l in data]

configured = []
for line in data:
    configured.append(line.rstrip("\n"))

for line in range(len(configured)):
    for char in range(len(configured[line])):
        complete[line].append([line, char, configured[line][char]])

for i in complete:
    for j in i:
        if j[2] == "S":
            animal = j

b = len(configured[0])
def check(row, column):
    N = complete[row-1][column] if row != 0 else ["."]
    E = complete[row][column+1] if column != int(b) - 1 else ["."]
    S = complete[row+1][column] if row != len(complete)-1 else ["."]
    W = complete[row][column-1] if column != 0 else ["."]
    return N, E, S, W
current = animal
direction = "all"
print(complete)
while True:
    print(complete[current[0]][current[1]], "hi")
    if len(current) == 3:
        current[2] = complete[current[0]][current[1]][2]
    x = check(current[0], current[1])
    for i in range(len(x)):
        if i == 0:
            try:
                if x[i][2] in ["|", "7", "F"] and direction in "all, north":
                    if x[i][2] == "|":
                        direction = "north"
                    elif x[i][2] == "7":
                        direction = "west"
                    elif x[i][2] == "F":
                        direction = "east"
                    current[0] = current[0]-1
                    x = check(current[0], current[1])                
                    break
            except IndexError:
                pass
        elif i == 1:
            try:
                if x[i][2] in ["-", "7", "J"] and direction in "all, east":
                    if x[i][2] == "-":
                        direction = "east"
                    elif x[i][2] == "7":
                        direction = "south"
                    elif x[i][2] == "J":
                        direction = "north"
                    current[1] = current[1]+1
                    x = check(current[0], current[1])                
                    break
            except IndexError:
                pass
        elif i == 2:
            try:
                if x[i][2] in ["|", "L", "J"] and direction in "all, south":
                    if x[i][2] == "|":
                        direction = "south"
                    elif x[i][2] == "L":
                        direction = "east"
                    elif x[i][2] == "J":
                        direction = "west"
                    current[0] = current[0]+1
                    x = check(current[0], current[1])                
                    break
            except IndexError:
                pass
        else:
            try:
                if x[i][2] in ["-", "F", "L"] and direction in "all, west":
                    if x[i][2] == "-":
                        direction = "west"
                    elif x[i][2] == "L":
                        direction = "north"
                    elif x[i][2] == "F":
                        direction = "south"
                    current[1] = current[1]-1
                    x = check(current[0], current[1])                
                    break
            except IndexError:
                pass
