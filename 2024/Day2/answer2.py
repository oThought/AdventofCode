data = open("data.txt", "r")
text = data.readlines()

total = 0
for lineStr in text:
  
    lineList = lineStr.split()
    for l in range(len(lineList)):
        lineList[l] = int(lineList[l])
    options = [lineList]
    for i in range(len(lineList)):
        newLine = lineList.copy()
        newLine.pop(i)
        options.append(newLine)
    
    for line in options:
        unsafe = False
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
        else:
            total = total + 1
            break

print(total)
