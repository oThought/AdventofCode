# AdventOfCode/2022/day01/solution.py
# 
# Snack Calories
# 
# https://adventofcode.com/2022/day/1


def main(input_name):
    input_file = open(input_name)
    input_text = input_file.read().strip()
    result1 = part1(input_text)
    result2 = part2(input_text)
    print(result1, result2)


def part1(input_text):
    all_elf_list = get_all_elves(input_text)
    return max(all_elf_list)


def part2(input_text):
    all_elf_list = get_all_elves(input_text)
    return sum(sorted(all_elf_list, reverse=True)[:3])


def get_all_elves(input_text):
    elf_text_list = input_text.split("\n\n")
    all_elves = []
    for elf_text in elf_text_list:
        elf_total = sum([int(number) for number in elf_text.split("\n")])
        all_elves.append(elf_total)
    return all_elves


main("example.txt")
main("input.txt")
