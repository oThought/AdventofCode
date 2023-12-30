f = open("Data.txt", "r")
data = f.readlines()

times = data[0].split(":")[1].rstrip("\n").split()
distance = data[1].split(":")[1].rstrip("\n").split()

output = 1
for time in range(len(times)):
    total = 0
    for charge in range(int(times[time]) + 1):
        if charge * (int(times[time]) - charge) > int(distance[time]):
            total += 1
    output *= total

print(output)