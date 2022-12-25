# AdventOfCode/2022/day05/solution.py
# 
# --- Day 5: Supply Stacks ---
# 
# https://adventofcode.com/2022/day/5


from copy import deepcopy


def main(input_name):
    input_file = open(input_name)
    input_text = input_file.read().rstrip()
    input_data = parse_input(input_text)
    result1 = calc_part1(input_data)
    result2 = calc_part2(input_data)
    print(result1, result2)


def parse_input(input_text):
    grid_t, moves_t = input_text.split("\n\n")
    grid = parse_grid(grid_t)
    moves = parse_moves(moves_t) 
    return grid, moves


def parse_grid(grid_text):
    layers = grid_text.split("\n")[:-1][::-1]
    count = (len(layers[0]) + 1) // 4
    grid = [[] for _ in range(count)]
    for layer in layers:
        for col in range(count):
            letter = layer[4 * col + 1]
            if letter != " ":
                grid[col].append(letter)
    return grid


def parse_moves(moves_text):
    return [parse_move(move_text) for move_text in moves_text.split("\n")]


def parse_move(move_text):
    _, num_t, _, col1_t, _, col2_t = move_text.split(" ")       
    return (int(num_t), int(col1_t) - 1, int(col2_t) - 1)


def calc_part1(input_data):
    grid, moves = input_data
    grid = deepcopy(grid)
    for (num, col1, col2) in moves:
        for _ in range(num):
            grid[col2].append(grid[col1].pop())
    return "".join(col[-1] for col in grid)


def calc_part2(input_data):
    grid, moves = input_data
    grid = deepcopy(grid)
    for (num, col1, col2) in moves:
        grid[col2] += grid[col1][-num:]
        grid[col1] =  grid[col1][:-num]
    return "".join(col[-1] for col in grid)


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
