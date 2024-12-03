from py.util import read_input, parse_matrix

# read in data
input_str: str = read_input("input2")

# parse into nested list of ints
data: list[list[int]] = parse_matrix(input_str.split("\n"))

# separate into two lists
list1: list[int] = [row[0] for row in data]
list2: list[int] = [row[1] for row in data]
# print(data[0:10])

# calculate differences
def calc_diffs(list1: list[int], list2: list[int]) -> list[int]:
    list1.sort()
    list2.sort()
    return [abs(x1 - x2) for x1, x2 in zip(list1, list2)]

diffs: list[int] = calc_diffs(list1, list2)
# print(diffs[0:10])

# part 1 solution
def part1() -> int:
    return sum(diffs)

print(f"result 1: {part1()}\n")

## part 2
def calc_sim_scores(left: list[int], right: list[int]) -> list[int]:
    return [x * right.count(x) for x in left]

sims: list[int] = calc_sim_scores(list1, list2)
# print(sims[0:10])

# part 2 solution
def part2() -> int:
    return sum(sims)

print(f"result 2: {part2()}")













