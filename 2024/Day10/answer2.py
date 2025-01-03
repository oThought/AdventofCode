data = open("data.txt", "r")
text = data.readlines()
# j = row number
grid = {i+j*1j: int(c) for i,r in enumerate(text) for j,c in enumerate(r.strip())}

# recursive code
def search(pos, height=0):
    if pos in grid and grid[pos] == height:
        if height < 9: # doesnt mark 9 as complete, so it can be counted multiple times
            return sum(search(pos+n, height+1) for n in [1,-1,1j,-1j])
        return 1
    return 0

print(sum(search(pos) for pos in grid if grid[pos]==0))