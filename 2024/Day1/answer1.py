data = open("data.txt", "r")
text = data.readlines()

firsts = []
seconds = []
for line in text:
    first, second = line.split()
    firsts.append(int(first))
    seconds.append(int(second))

firsts.sort()
seconds.sort()
total = 0
for number in range(len(text)):
    distance = abs(firsts[number] - seconds[number])
    total = total + distance

print(total)
    
    