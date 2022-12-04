# AdventOfCode/2022/day02/solution.py
# 
# Snack Calories
# 
# https://adventofcode.com/2022/day/2


def main(input_name):
    input_file = open(input_name)
    input_text = input_file.read().strip()
    result1 = part1(input_text)
    result2 = part2(input_text)
    print(result1, result2)


def part1(input_text):
    rounds = input_text.split("\n")
    total_score = 0
    dict = {"X": 1, "Y": 2, "Z": 3}
    for round in rounds:
        players = round.split(" ")
        if players[0] == "A" and players[1] == "Z" or players[0] == "B" and players[1] == "X" or players[0] == "C" and players[1] == "Y":
            total_score += 0 + dict[players[1]]
        elif players[0] == "A" and players[1] == "X" or players[0] == "B" and players[1] == "Y" or players[0] == "C" and players[1] == "Z":
            total_score += 3 + dict[players[1]]
        elif players[0] == "A" and players[1] == "Y" or players[0] == "B" and players[1] == "Z" or players[0] == "C" and players[1] == "X":
            total_score += 6 + dict[players[1]]
    return total_score


def part2(input_text):
    rounds = input_text.split("\n")
    total_score = 0
    dict = {"X":{"A": 2, "B": 3, "C": 1}, "Y":{"A": 4, "B": 5, "C": 6}, "Z":{"A": 9, "B": 7, "C": 8}}
    for round in rounds:
        players = round.split(" ")
        total_score += 0 + dict[players[1]][players[0]] 
    return total_score

main("example.txt")
main("input.txt")
