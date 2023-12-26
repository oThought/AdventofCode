f = open("Data.txt", "r")
data = f.readlines()

total = 0
for line in data:
    gameNumber, colours = line.split(": ")
    gameNumber = int(gameNumber[5:])
    sections = colours.split("; ")
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
            if red > 12 or blue > 14 or green > 13:
                gameNumber = 0
                break
        if gameNumber == 0:
            break
    print(gameNumber)
    total += gameNumber

print(total)