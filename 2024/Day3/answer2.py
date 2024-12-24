data = open("data.txt", "r")
text = data.readlines()

line = ""
total = 0
for t in text:
    line = line + t
current = 0
current1 = 0
current2 = 0
line2 = line
line3 = line
line4 = line
positions = []
does = [0]
donts = [-1]

while True:
    position = line.find("mul(")
    if position == -1:
        break
    positions.append(position+current)
    current += position+1
    line = line[position+1:]

while True:
    do = line3.find("do()")
    if do == -1:
        break
    does.append(do+current1)
    current1 += do+1
    line3 = line3[do+1:]
    
while True:
    dont = line4.find("don't()")
    if dont == -1:
        break
    donts.append(dont+current2)
    current2 += dont+1
    line4 = line4[dont+1:]

does.append(1000000000000000)
donts.append(1000000000000000)    

for p in positions:
    for a in range(len(does)):
        if does[a] > p: 
            closestDo = does[a-1]
            break
    for b in range(len(donts)):
        if donts[b] > p: 
            closestDont = donts[b-1]
            break
    print(closestDo, closestDont, p)
    if closestDont > closestDo:
        continue
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