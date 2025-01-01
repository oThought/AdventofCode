from collections import deque
data = open("test.txt", "r")
text = data.readlines()[0].replace("\n", "")
lengths = [int(num) for num in text]

filled = deque()
gaps = deque()
actual = 0
for i, num in enumerate(lengths): # convert 12345 --> 0..111...22222
    if i % 2 == 0:
        filled.append([i//2, actual, num]) # num, position, length
    else:
        if num > 0:
            gaps.append([actual, num])
    actual += num

moved = deque()
while True: # convert 0..111...22222 --> 022111222
    gPos, gLen = gaps.popleft()
    fId, fPos, fLen = filled.pop()
    if gPos > fPos: # last case
        filled.append([fId,fPos,fLen])
        break
    if gLen > fLen: # larger space than file length
        moved.append([fId,gPos,fLen])
        gaps.appendleft([gPos+fLen,gLen-fLen])
    elif gLen == fLen: # same space
        moved.append([fId,gPos,fLen])
    else: # smaller space than file length
        moved.append([fId,gPos,gLen])
        filled.append([fId,fPos,fLen-gLen])
    
final = filled + moved
print(final)
answer = sum(num*(start*length+(length*(length-1))//2) for num,start,length in final)
print(answer)