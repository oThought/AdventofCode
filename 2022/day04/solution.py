# AdventOfCode/2022/day04/solution.py
# 
# --- Day 4: Camp Cleanup ---
# 
# https://adventofcode.com/2022/day/4


def main(input_name):
    input_file = open(input_name)
    input_text = input_file.read().rstrip()
    input_data = parse_input(input_text)
    result1 = calc_part1(input_data)
    result2 = calc_part2(input_data)
    print(result1, result2)


def parse_input(input_text):
    return [parse_line(line) for line in input_text.split("\n")]


def parse_line(line_text):
    p1_t, p2_t = line_text.split(",")
    p1s_t, p1e_t = p1_t.split("-")
    p2s_t, p2e_t = p2_t.split("-")
    return (int(p1s_t), int(p1e_t)), (int(p2s_t), int(p2e_t))


def calc_part1(input_data):
    return sum(contains(p1, p2) for (p1, p2) in input_data)


def calc_part2(input_data):
    return sum(overlaps(p1, p2) for (p1, p2) in input_data)


def contains(p1, p2):
    ol = overlap(p1, p2)
    return int(width(p1) == width(ol) or width(p2) == width(ol))


def overlaps(p1, p2):
    ol = overlap(p1, p2)
    return int(width(ol) >= 1)


def width(p):
    return max(0, 1 + p[1] - p[0])


def overlap(p1, p2):
    return max(p1[0], p2[0]), min(p1[1], p2[1])


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
