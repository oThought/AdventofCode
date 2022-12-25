# AdventOfCode/2022/day02/solution.py
# 
# --- Day 2: Rock Paper Scissors ---
# 
# https://adventofcode.com/2022/day/2


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
    return line_text


def calc_part1(input_data):
    total_score = 0
    dict = {"X": 1, "Y": 2, "Z": 3}
    for round in input_data:
        players = round.split(" ")
        if players[0] == "A" and players[1] == "Z" or players[0] == "B" and players[1] == "X" or players[0] == "C" and players[1] == "Y":
            total_score += 0 + dict[players[1]]
        elif players[0] == "A" and players[1] == "X" or players[0] == "B" and players[1] == "Y" or players[0] == "C" and players[1] == "Z":
            total_score += 3 + dict[players[1]]
        elif players[0] == "A" and players[1] == "Y" or players[0] == "B" and players[1] == "Z" or players[0] == "C" and players[1] == "X":
            total_score += 6 + dict[players[1]]
    return total_score


def calc_part2(input_data):
    total_score = 0
    dict = {"X":{"A": 3, "B": 1, "C": 2}, "Y":{"A": 4, "B": 5, "C": 6}, "Z":{"A": 8, "B": 9, "C": 7}}
    for round in input_data:
        players = round.split(" ")
        total_score += dict[players[1]][players[0]] 
    return total_score


if __name__ == "__main__":
    main("example.txt")
    main("input.txt")
