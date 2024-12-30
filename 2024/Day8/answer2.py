from math import gcd
data = open("data.txt", "r")
text = data.readlines()

grid = []
antinodes = []
for row in range(len(text)):
    grid.append([])
    antinodes.append([])
    for column in range(len(text[row])):
        grid[row].append(text[row][column])
        antinodes[row].append(False)
for a in range(len(grid)-1):
    grid[a].pop(-1)
    antinodes[a].pop(-1)

antennas = {}
for line in range(len(grid)):
    for b in range(len(grid[line])):
        if grid[line][b] == ".":
            continue
        if antennas.get(text[line][b], 1) == 1:
            antennas[text[line][b]] = [[line, b]]
        else:
            antennas[text[line][b]] = antennas[text[line][b]] + [[line, b]]

def outside(rw, clm):
    global antinodes
    return True if rw < 0 or rw > len(antinodes)-1 or clm < 0 or clm > len(antinodes[1])-1 else False

for antenna in antennas.values():
    for c in range(len(antenna)):
        for d in range(c+1, len(antenna)):
            dR, dC = antenna[c][0] - antenna[d][0], antenna[c][1] - antenna[d][1]
            commonDivisor = gcd(abs(dR), abs(dC))
            dR, dC = dR // commonDivisor, dC // commonDivisor
            cX, cY, c2X, c2Y = antenna[c][0], antenna[c][1], antenna[c][0], antenna[c][1]
            while not outside(cX, cY):
                antinodes[cX][cY] = True
                cX, cY = cX + dR, cY + dC
            while not outside(c2X, c2Y):
                antinodes[c2X][c2Y] = True
                c2X, c2Y = c2X - dR, c2Y - dC

total = 0         
for e in antinodes:
    for f in e:
        total = total + 1 if f else total

print(total)