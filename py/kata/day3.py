import math
import regex as re

from py.util import read_input

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
    # get list of all strings after a "do()", chop at "don't" if present
    lines: list[str] = [line.split("don't()")[0] for line in input_str.split("do()")]

    # parse each mul instruction out of each do line
    instructions: list[tuple[int, int]] = [(int(x), int(y)) for line in lines for x, y in re.findall("mul\((\d+),(\d+)\)", line)]
    # print(f"instructions: {instructions}")

    # calculate products
    results: list[int] = [math.prod(instruction) for instruction in instructions]

    # calculate final sum
    return sum(results)

print(f"result 2: {part2()}")













