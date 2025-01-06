grid = {i+j*1j: c for i,r in enumerate(open('data.txt')) for j,c in enumerate(r.strip())}

regions = {p: {p} for p in grid}
print(regions)

for p in grid:
    for n in p+1, p-1, p+1j, p-1j:
        if n in grid and grid[p] == grid[n]:
            regions[p] |= regions[n]
            for x in regions[p]: 
                regions[x] = regions[p]
regions = {tuple(r) for r in regions.values()}

for r in regions:
    print(r)

def edge(reg):
    output = []
    for p in reg: 
        for pair in ((+1, +1j), (+1j, -1), (-1, -1j), (-1j, +1)):
            # exterior
            if p+pair[0] not in reg and p+pair[1] not in reg:
                output.append(p)
            # interior
            if p+pair[0] in reg and p+pair[1] in reg and p+pair[0]+pair[1] not in reg:
                output.append(p)
    return output

print(sum(len(r) * len(edge(r)) for r in regions))
