data = open("data.txt", "r")
text = data.readlines()

total = 0
for lineStr in text:

    unsafe = False
    line = lineStr.split()

    for l in range(len(line)):
        line[l] = int(line[l])

    if line[0] > line[-1]:
        for number in range(len(line)-1):
            if line[number] <= line[number+1]:
                unsafe = True
    if line[0] < line[-1]:
        for number in range(len(line)-1):
            if int(line[number]) >= int(line[number+1]):
                unsafe = True
    if line[0] == line[-1]:
        unsafe = True
    for number in range(len(line)-1):
        if abs(int(line[number]) - int(line[number+1])) > 3:
            unsafe = True

    if unsafe:
        continue
    total = total + 1

print(total)
