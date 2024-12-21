data = open("data.txt", "r")
text = data.readlines()

firsts = []
seconds = []
for line in text:
    first, second = line.split()
    firsts.append(int(first))
    seconds.append(int(second))

total = 0
for i in range(len(text)):
    number = firsts[i]
    score = seconds.count(number) * number
    total = total + score

print(total)
