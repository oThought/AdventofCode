data = open("test.txt", "r")
text = data.readlines()

a = [] # [[row, column]]
for row in range(len(text)):
    for column in range(len(text[row])):
        if text[row][column] == "A":
            a.append([row, column])

def check(r, c, letter):
    if r < 0 or c < 0:
        return False
    try:
        return True if text[r][c] == letter else False
    except IndexError:
        return False

total = 0
for pos in a:
    total = total + 1 if check(pos[0]-1, pos[1]-1, "M") and check(pos[0]-1, pos[1]+1, "M") and check(pos[0]+1, pos[1]+1, "S") and check(pos[0]+1, pos[1]-1, "S") else total
    total = total + 1 if check(pos[0]-1, pos[1]-1, "S") and check(pos[0]-1, pos[1]+1, "M") and check(pos[0]+1, pos[1]+1, "M") and check(pos[0]+1, pos[1]-1, "S") else total
    total = total + 1 if check(pos[0]-1, pos[1]-1, "S") and check(pos[0]-1, pos[1]+1, "S") and check(pos[0]+1, pos[1]+1, "M") and check(pos[0]+1, pos[1]-1, "M") else total
    total = total + 1 if check(pos[0]-1, pos[1]-1, "M") and check(pos[0]-1, pos[1]+1, "S") and check(pos[0]+1, pos[1]+1, "S") and check(pos[0]+1, pos[1]-1, "M") else total

print(total)