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
            if not outside(antenna[c][0]+dR, antenna[c][1]+dC):
                antinodes[antenna[c][0]+dR][antenna[c][1]+dC] = True
            if not outside(antenna[d][0]-dR, antenna[d][1]-dC):
                antinodes[antenna[d][0]-dR][antenna[d][1]-dC] = True

total = 0         
for e in antinodes:
    for f in e:
        total = total + 1 if f else total

print(total)