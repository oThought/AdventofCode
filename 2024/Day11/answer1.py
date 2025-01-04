from collections import deque
from math import floor, log10
data = open("data.txt", "r")
text = data.readlines()[0].split(" ")
text = deque([int(num) for num in text])
memo = {}

for i in range(75):
    print(i)
    for num in range(len(text)):
        number = text.popleft()
        string = str(number)
        if number in memo:
            for item in memo[number]:
                text.append(item)
        else:
            if number == 0:
                text.append(1)
            elif len(string) % 2 == 0:
                l = floor(log10(number))+1
                if l % 2 == 0:
                    text.append(number // 10**(l//2))
                    text.append(number % 10**(l//2))
            else:
                text.append(number * 2024)
print(len(text))