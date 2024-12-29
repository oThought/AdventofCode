import copy
data = open("test.txt", "r")
text = data.readlines()
grid = []
dir = {"^": "w", ">": "d", "v": "s", "<": "a"}
repeatGrid = []
for row in range(len(text)):
    grid.append([])
    repeatGrid.append([])
    for column in range(len(text[row])):
        repeatGrid[row].append(False)
        grid[row].append(text[row][column])

for a in range(len(grid)-1):
    grid[a].pop(-1)

for b in range(len(grid)):
    for c in range(len(grid[b])):
        if grid[b][c] == "^":
            posRow, posColumn = b, c

cPosRow, cPosColumn, cRepeatGrid = copy.deepcopy(posRow), copy.deepcopy(posColumn), copy.deepcopy(repeatGrid)

def outside(pRow, pColumn):
    return True if pRow < 0 or pRow > len(grid) - 1 or pColumn < 0 or pColumn > len(grid[1]) - 1 else False

def checkGrid(grid, posRow, posColumn, repeats):
    while not outside(posRow, posColumn):
        d, e = posRow, posColumn
        direction = grid[posRow][posColumn]
        if direction == "^":
            if not outside(posRow-1, posColumn) and grid[posRow-1][posColumn] == "#":
                if not outside(posRow, posColumn+1):
                    grid[posRow][posColumn+1] = ">"
                posColumn = posColumn + 1
            else:
                if not outside(posRow-1, posColumn):
                    if repeats:
                        print(dir[direction], grid[posRow-1][posColumn], posRow, posColumn)
                        if dir[direction] == grid[posRow-1][posColumn]:
                            if repeatGrid[posRow-1][posColumn]:
                                return True
                            repeatGrid[posRow-1][posColumn] = True
                    grid[posRow-1][posColumn] = "^"
                posRow = posRow - 1   
            grid[d][e] = "w"   
        elif direction == ">":
            if not outside(posRow, posColumn+1) and grid[posRow][posColumn+1] == "#":
                if not outside(posRow+1, posColumn):
                    grid[posRow+1][posColumn] = "v"
                posRow = posRow + 1
            else:
                if not outside(posRow, posColumn+1):
                    if repeats:
                        print(dir[direction], grid[posRow][posColumn+1], posRow, posColumn)
                        if dir[direction] == grid[posRow][posColumn+1]:
                            if repeatGrid[posRow][posColumn+1]:
                                return True
                            repeatGrid[posRow][posColumn+1] = True
                    grid[posRow][posColumn+1] = ">"
                posColumn = posColumn + 1      
            grid[d][e] = "d" 
        elif direction == "v":
            if not outside(posRow+1, posColumn) and grid[posRow+1][posColumn] == "#":
                if not outside(posRow, posColumn-1):
                    grid[posRow][posColumn-1] = "<"
                posColumn = posColumn - 1
            else:
                if not outside(posRow+1, posColumn):
                    if repeats:
                        print(dir[direction], grid[posRow+1][posColumn], posRow, posColumn)
                        if dir[direction] == grid[posRow+1][posColumn]:
                            if repeatGrid[posRow+1][posColumn]:
                                return True
                            repeatGrid[posRow+1][posColumn] = True
                    grid[posRow+1][posColumn] = "v"
                posRow = posRow+1  
            grid[d][e] = "s"      
        elif direction == "<":
            if not outside(posRow, posColumn-1) and grid[posRow][posColumn-1] == "#":
                if not outside(posRow-1, posColumn):
                    grid[posRow-1][posColumn] = "^"
                posRow = posRow - 1
            else:
                if not outside(posRow, posColumn-1):
                    if repeats:
                        print(dir[direction], grid[posRow][posColumn-1], posRow, posColumn)
                        if dir[direction] == grid[posRow][posColumn-1]:
                            if repeatGrid[posRow][posColumn-1]:
                                return True
                            repeatGrid[posRow][posColumn-1] = True
                    grid[posRow][posColumn-1] = "<"
                posColumn = posColumn - 1       
            grid[d][e] = "a" 

checkGrid(grid, posRow, posColumn, False)
possible = []
for line in range(len(grid)):
    for f in range(len(grid[line])):
        if grid[line][f] in "wasd":
            possible.append([line, f])

print(possible)
total = 0
for g in possible:
    posRow, posColumn, repeatGrid = cPosRow, cPosColumn, cRepeatGrid
    grid[posRow][posColumn] = "^"
    grid[g[0]][g[1]] = "#"
    if checkGrid(grid, posRow, posColumn, True):
        print("hi")
        total = total + 1   
    grid[g[0]][g[1]] = "."

print(total) 