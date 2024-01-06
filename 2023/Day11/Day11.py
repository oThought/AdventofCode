import copy
f = open("Data.txt", "r")
data = f.readlines()

for d in range(len(data)):
    data[d] = data[d].rstrip('\n')
length = len(data[0])
universe = [["" for i in range(len(l))] for l in data]

for line in range(len(data)):
    for char in range(len(data[line])):
        universe[line][char] = data[line][char]

z = 0
dupe = copy.deepcopy(universe)
for line in range(len(dupe)):
    try:
        x = dupe[line].index("#")
    except ValueError:
        universe.insert(line+1+z, dupe[line])
        z += 1

columbs = [["" for l in universe] for i in range(length)]
for line in range(len(universe)):
    for char in range(len(universe[line])):
        columbs[char][line] = universe[line][char]

z = 0
dupetwo = copy.deepcopy(columbs)
for line in range(len(dupetwo)):
    try:
        y = dupetwo[line].index("#")
    except ValueError:
        columbs.insert(line+1+z, dupetwo[line])
        z += 1

galaxies = []
for i in range(len(columbs)):
    for j in range(len(columbs[i])):
        if columbs[i][j] == "#":
            galaxies.append([j, i])

def findDistance(xOne, yOne, xTwo, yTwo):
    return abs(xTwo - xOne) + abs(yTwo - yOne)

h = 0
for i in range(len(galaxies)):
    for j in range(len(galaxies[i+1:])):
        k = findDistance(galaxies[i][0], galaxies[i][1], galaxies[i+1:][j][0], galaxies[i+1:][j][1])
        # print(k, galaxies[i], galaxies[i+1:][j])
        h += k

print(h)
