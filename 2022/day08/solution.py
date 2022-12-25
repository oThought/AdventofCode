# AdventOfCode/2022/day08/solution.py
# 
# --- Day 8: Treetop Tree House ---
# 
# https://adventofcode.com/2022/day/8


def main(input_name):
    input_file = open(input_name)
    input_text = input_file.read().rstrip()
    input_data = parse_input(input_text)
    result1 = calc_part1(input_data)
    result2 = calc_part2(input_data)
    print(result1, result2)


def parse_input(input_text):
    return [parse_line(line_text) for line_text in input_text.split("\n")]


def parse_line(line_text):
    return [int(char) for char in line_text]


def calc_part1(inp_grid):
    vis_grid = [[0] * len(inp_grid[0]) for _ in inp_grid]
    for _ in range(4):
        inp_grid = rotate_grid(inp_grid)
        vis_grid = rotate_grid(vis_grid)
        get_visible_grid(inp_grid, vis_grid)
    return sum(sum(vis_cells) for vis_cells in vis_grid)


def calc_part2(inp_grid):
    return


def get_visible_grid(inp_grid, vis_grid):
    for row in range(len(inp_grid)):
        get_visible_cells(inp_grid[row], vis_grid[row])


def get_visible_cells(inp_cells, vis_cells):
    highest = -1
    for col in range(len(inp_cells)):
        if inp_cells[col] > highest:
            vis_cells[col] = 1
            highest = inp_cells[col]
    return vis_cells   


def rotate_grid(old_grid):
    rows = len(old_grid)
    cols = len(old_grid[0])
    new_grid = [[0] * rows for _ in range(cols)]
    for row in range(rows):
        for col in range(cols):
            new_grid[col][rows-row-1] = old_grid[row][col]
    return new_grid


def print_grid(grid):
    for cells in grid:
        for cell in cells:
            print(f"{cell:3d}", end="")
        print()
    print()


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
