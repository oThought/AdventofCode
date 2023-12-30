f = open("Data.txt", "r")
data = f.readlines()

time = data[0].split(":")[1].strip()
distance = data[1].split(":")[1].strip()

print(time, distance)

total = 0
for charge in range(int(time) + 1):
    if charge * (int(time) - charge) > int(distance):
        total += 1

print(total)