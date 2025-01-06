grid = {i+j*1j: c for i,r in enumerate(open('test.txt')) for j,c in enumerate(r.strip())}

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

def perimeter(reg):
    return {(p,d) for d in (+1,-1,+1j,-1j) for p in reg if p+d not in reg}
            
print(sum(len(r) * len(perimeter(r)) for r in regions))