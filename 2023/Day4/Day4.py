f = open("Data.txt", "r")
data = f.readlines()

games = {}
for line in range(len(data)):
    games[line+1] = 1

for line in data:
    game, numbers = line.split(": ")
    winning, scratch = numbers.split(" | ")
    winning = winning.split()
    scratch = scratch.split()
    for i in range(games[data.index(line)+1]):
        current = 0
        for number in scratch:
            if str(number) in winning:
                if current == 0:
                    current = 1
                else:
                    current += 1
        duplicates = []
        for j in range(current):
            duplicates.append(data.index(line)+1+j+1)   
        for duplicate in duplicates:
            try:
                games[duplicate] = games[duplicate] + 1
            except KeyError:
                pass

print(games)
total = []
for key in games.keys():
	total.append(games[key])
     
print(sum(total))