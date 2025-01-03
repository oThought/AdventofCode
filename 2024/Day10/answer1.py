data = open("data.txt", "r")
text = data.readlines()
# j = row number
grid = {i+j*1j: int(c) for i,r in enumerate(text) for j,c in enumerate(r.strip())}

# recursive code
def search(pos, seen, height=0):
    if pos in grid and grid[pos] == height:
        if height < 9 or pos in seen: # checks for individual 9
            return sum(search(pos+n, seen, height+1) for n in [1,-1,1j,-1j])
        seen.add(pos)
        return 1
    return 0

print(sum(search(pos, set()) for pos in grid if grid[pos]==0))