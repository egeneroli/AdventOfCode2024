import math
import regex as re
# import re

from py.util import read_input, parse_matrix

# read in data
input_str: str = read_input("input3", False)

# part 1 solution
def part1() -> int:
    # use regex to match all mul instructions
    matches: list[str] = re.findall("(?<=mul\()\d+,\d+(?=\))", input_str)
    # print(f"matches: {matches}")

    # parse each mul instruction
    instructions: list[list[int]] = [[int(num) for num in re.findall("\d+", match)] for match in matches]
    # print(f"instructions: {instructions}")

    # calculate products
    results: list[int] = [math.prod(instruction) for instruction in instructions]

    # calculate final sum
    return sum(results)

print(f"result 1: {part1()}\n")


## part 2
# part 2 solution
def part2() -> int:
    # use regex to match all mul instructions
    data: str = f"do(){input_str}don't()"
    # print(f"input: {data}")
    # matches: list[str] = re.findall("(?<=do\(\))[^d]*(?:[^d]|d(?!on't))*mul\(\d+,\d+\)", data)
    matches: list[str] = re.findall("(do\(\)).*?(mul\(\d+,\d+\).*?)+", data)
    # pattern = re.compile("(?:do\(\))(.*?(?:mul\(\d+,\d+\)))+")
    # matches = []
    # lst: list = [match for match in pattern.finditer(data)]
    # for match in lst[:1]:
    #     # matches.extend(re.findall("mul\(\d+,\d+\)", match.group(0)))
    #     print(match.allcaptures()[:1])

    # matches: list[str] = [x for match in re.findall("(?<=do\(\)).*?(?=do)", data) for x in re.findall("mul\(\d+,\d+\)", match)]
    print(f"matches: {matches.__len__()}")
    for match in matches[:3]:
        print(f"match: {match}")

    # # parse each mul instruction
    # instructions: list[list[int]] = [[int(num) for num in re.findall("\d+", match)] for match in matches]
    # # print(f"instructions: {instructions}")
    #
    # # calculate products
    # results: list[int] = [math.prod(instruction) for instruction in instructions]
    #
    # # calculate final sum
    # return sum(results)

print(f"result 2: {part2()}")













