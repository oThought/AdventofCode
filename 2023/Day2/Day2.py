f = open("Data.txt", "r")
data = f.readlines()

total = 0
for line in data:
    gameNumber, colours = line.split(": ")
    gameNumber = int(gameNumber[5:])
    sections = colours.split("; ")
    max = [0, 0, 0]
    for section in sections:
        section = section.split(", ")
        for colour in section:
            if "red" in colour:
                red = int(colour[0:2].rstrip())
            else:
                red = 0
            if "blue" in colour:
                blue = int(colour[0:2].rstrip())
            else: 
                blue = 0
            if "green" in colour:
                green = int(colour[0:2].rstrip())
            else: 
                green = 0
       
            if red > max[0]:
                max[0] = red
            if blue > max[1]:
                max[1] = blue
            if green > max[2]:
                max[2] = green
    power = max[0] * max[1] * max[2]
    total += power

print(total)