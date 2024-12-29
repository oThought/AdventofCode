data = open("data.txt", "r")
text = data.readlines()

total = 0
for line in text:
    # splits the output from the inputs, then finds all base2 permutations for the product
    output, inputs = line.split(":")
    output, inputs = int(output.strip()), inputs.split()
    length = len(inputs)-1
    options = [''.join(str((i // (2**j)) % 2) for j in range(length - 1, -1, -1)) for i in range(2**length)]
    # finds all possible outcomes and totals the correct outputs
    results = []
    for option in options:
        result = int(inputs[0])
        for i, command in enumerate(option):
            result = result + int(inputs[i+1]) if command == "0" else result * int(inputs[i+1])
        results.append(result)
    total = total + output if output in results else total

print(total)

