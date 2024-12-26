data = open("data.txt", "r")
text = data.readlines()

x = [] # [[row, column]]
for row in range(len(text)):
    for column in range(len(text[row])):
        if text[row][column] == "X":
            x.append([row, column])

def check(r, c, letter):
    if r < 0 or c < 0:
        return False
    try:
        return True if text[r][c] == letter else False
    except IndexError:
        return False

total = 0
for pos in x:
    total = total + 1 if check(pos[0]-1, pos[1]-1, "M") and check(pos[0]-2, pos[1]-2, "A") and check(pos[0]-3, pos[1]-3, "S") else total
    total = total + 1 if check(pos[0], pos[1]-1, "M") and check(pos[0], pos[1]-2, "A") and check(pos[0], pos[1]-3, "S") else total
    total = total + 1 if check(pos[0]+1, pos[1]-1, "M") and check(pos[0]+2, pos[1]-2, "A") and check(pos[0]+3, pos[1]-3, "S") else total
    total = total + 1 if check(pos[0]+1, pos[1], "M") and check(pos[0]+2, pos[1], "A") and check(pos[0]+3, pos[1], "S") else total
    total = total + 1 if check(pos[0]+1, pos[1]+1, "M") and check(pos[0]+2, pos[1]+2, "A") and check(pos[0]+3, pos[1]+3, "S") else total
    total = total + 1 if check(pos[0], pos[1]+1, "M") and check(pos[0], pos[1]+2, "A") and check(pos[0], pos[1]+3, "S") else total
    total = total + 1 if check(pos[0]-1, pos[1]+1, "M") and check(pos[0]-2, pos[1]+2, "A") and check(pos[0]-3, pos[1]+3, "S") else total
    total = total + 1 if check(pos[0]-1, pos[1], "M") and check(pos[0]-2, pos[1], "A") and check(pos[0]-3, pos[1], "S") else total
      
print(total)