from collections import deque
data = open("data.txt", "r")
text = data.readlines()[0].split(" ")
text = deque([int(num) for num in text])
memo = {}

for i in range(25):
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
                middle = len(string) // 2
                text.append(int(string[:middle]))
                memo[number] = [int(string[:middle])]
                if string[middle:].lstrip("0") == "":
                    text.append(0)
                    memo[number].append(0)
                else:
                    text.append(int(string[middle:].lstrip("0")))
                    memo[number].append(int(string[middle:].lstrip("0")))
            else:
                text.append(number * 2024)
print(len(text))