import re
f = open("Data.txt", "r")
data = f.read()
data = re.split(r'\n\s*\n', data)

starts, lefts, rights = [], [], []
instruction = data[0]

for i in data[1].splitlines():
    start, x, left, right = i.split()
    left = left.lstrip("(").rstrip(",")
    right = right.rstrip(")")
    starts.append(start)
    lefts.append(left)
    rights.append(right)

current = []
for j in starts:
    if j.find("A") == 2 or j.count("A") == 3:
        current.append(j)

def check(c):
    if c.find("Z") == 2 or c.count("Z") == 3:
        return False
    return True

new = []
for c in current:
    time = 0
    while check(c):
        for direction in instruction:
            if direction == "L":
                c = lefts[starts.index(c)]
            else:
                c = rights[starts.index(c)]
            time += 1
            if check(c) == False:
                break
    new.append(time)

print(new)