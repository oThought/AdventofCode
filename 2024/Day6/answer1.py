data = open("data.txt", "r")
text = data.readlines()
grid = []

for row in range(len(text)):
    grid.append([])
    for column in range(len(text[row])):
        grid[row].append(text[row][column])

for a in range(len(grid)-1):
    grid[a].pop(-1)

for b in range(len(grid)):
    for c in range(len(grid[b])):
        if grid[b][c] == "^":
            posRow, posColumn = b, c

def outside(pRow, pColumn):
    return True if pRow < 0 or pRow > len(grid) - 1 or pColumn < 0 or pColumn > len(grid[1]) - 1 else False

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
                grid[posRow-1][posColumn] = "^"
            posRow = posRow - 1      
    elif direction == ">":
        if not outside(posRow, posColumn+1) and grid[posRow][posColumn+1] == "#":
            if not outside(posRow+1, posColumn):
                grid[posRow+1][posColumn] = "v"
            posRow = posRow + 1
        else:
            if not outside(posRow, posColumn+1):
                grid[posRow][posColumn+1] = ">"
            posColumn = posColumn + 1      
    elif direction == "v":
        if not outside(posRow+1, posColumn) and grid[posRow+1][posColumn] == "#":
            if not outside(posRow, posColumn-1):
                grid[posRow][posColumn-1] = "<"
            posColumn = posColumn - 1
        else:
            if not outside(posRow+1, posColumn):
                grid[posRow+1][posColumn] = "v"
            posRow = posRow+1       
    elif direction == "<":
        if not outside(posRow, posColumn-1) and grid[posRow][posColumn-1] == "#":
            if not outside(posRow-1, posColumn):
                grid[posRow-1][posColumn] = "^"
            posRow = posRow - 1
        else:
            if not outside(posRow, posColumn-1):
                grid[posRow][posColumn-1] = "<"
            posColumn = posColumn - 1       
    grid[d][e] = "X"

total = 0
for line in grid:
    for item in line:
        if item == "X":
            total = total + 1

print(total)
