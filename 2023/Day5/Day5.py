import re
f = open("Data.txt", "r")
data = f.read()
data = re.split(r'\n\s*\n', data)

for section in data:

    if data.index(section) == 0:
        x, seeds = section.split(": ")
        seeds = seeds.split()
    else:
        lines = section.splitlines()
        lines.pop(0)
        d = []
        s = []
        r = []

        for line in lines:
            destinationStart, sourceStart, rangeVar = line.split()
            d.append(destinationStart)
            s.append(sourceStart)
            r.append(rangeVar)

        for seed in range(len(seeds)):
            closest = 10000000000000
            for source in range(len(s)):
                sc = int(s[source])
                diff = int(seeds[seed])-sc
                if diff >= 0 and diff < closest and diff <= int(r[source])-1:
                    closest = int(seeds[seed])-sc
                    start = source
            if closest != 10000000000000:
                seeds[seed] = int(seeds[seed]) + int(d[start]) - int(s[start])
            else:
                seeds[seed] = int(seeds[seed])

print(seeds)
print(min(seeds))