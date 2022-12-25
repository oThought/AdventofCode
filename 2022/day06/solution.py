# AdventOfCode/2022/day06/solution.py
# 
# --- Day 6: Tuning Trouble ---
# 
# https://adventofcode.com/2022/day/6


def main(input_name):
    input_file = open(input_name)
    input_text = input_file.read().rstrip()
    input_data = parse_input(input_text)
    result1 = calc_part1(input_data)
    result2 = calc_part2(input_data)
    print(result1, result2)


def parse_input(input_text):
    return input_text.split("\n")


def calc_part1(input_data):
    return [get_marker(line_data, 4) for line_data in input_data]


def calc_part2(input_data):
    return [get_marker(line_data, 14) for line_data in input_data]


def get_marker(line_data, width):
    for i in range(len(line_data) - width + 1):
        marker = line_data[i:i+width]
        if len(set(marker)) == width:
            return i + width
    return -1 


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
