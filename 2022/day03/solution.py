# AdventOfCode/2022/day03/solution.py
# 
# --- Day 3: Rucksack Reorganization ---
# 
# https://adventofcode.com/2022/day/3


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
    mid = len(line_text) // 2
    c1 = set(line_text[:mid])
    c2 = set(line_text[mid:])
    return (c1, c2)


def calc_part1(input_data):
    return sum(calc_priority1(c1, c2) for (c1, c2) in input_data) 


def calc_part2(input_data):
    return sum(calc_priority2(input_data[i: i+3]) 
            for i in range(0, len(input_data), 3)) 


def calc_priority1(c1, c2):
    return priority(list(c1.intersection(c2))[0])


def calc_priority2(group_data):
    group = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for (c1, c2) in group_data: 
        group = group.intersection(c1.union(c2))
    return priority(list(group)[0])


def priority(letter):
    if letter.islower():
        return ord(letter) - 96
    return ord(letter) - 64 + 26


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
