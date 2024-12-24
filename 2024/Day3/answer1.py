data = open("data.txt", "r")
text = data.readlines()

line = ""
total = 0
for t in text:
    line = line + t
current = 0
line2 = line
positions = []

while True:
    position = line.find("mul(")
    if position == -1:
        break
    positions.append(position+current)
    current += position+1
    line = line[position+1:]
    
for p in positions:
    
    for i in range(5, 1000):
        digits = line2[p+4:p+i]
        if not digits.isdigit():
            x = i
            break
    if line2[p+x-1] != ",":
        continue
    for i in range(1, 1000):
        digits2 = line2[p+x:p+x+i]
        if not digits2.isdigit():
            y = i
            break
    if line2[p+x+y-1] != ")":
        continue
    total = total + int(line2[p+4:p+x-1]) * int(line2[p+x:p+x+y-1])

print(total)