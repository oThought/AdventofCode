data = open("data.txt", "r")
text = data.readlines()

total = 0
for line in text:
    print(text.index(line))
    # splits the output from the inputs, then finds all base3 permutations for the product
    output, inputs = line.split(":")
    output, inputs = int(output.strip()), inputs.split()
    length = len(inputs)-1
    options = [''.join(str((i // (3**j)) % 3) for j in range(length - 1, -1, -1)) for i in range(3**length)]
    # finds all possible outcomes and totals the correct outputs        
    results = []
    for option in options:
        copy = inputs[:]
        result = int(inputs[0])
        for i, command in enumerate(option):
            if command == "0":
                result = result + int(copy[i+1])
            elif command == "1":
                result = int(str(result) + str(copy[i+1]))
            else:
                result = result * int(copy[i+1])
        results.append(result)
    total = total + output if output in results else total

print(total)