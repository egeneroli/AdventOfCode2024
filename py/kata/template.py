from py.util import read_input, parse_matrix

# read in data
lines: list[str] = read_input("input1")
print(f"input: {lines[0:10]}\n")

# parse into nested list of ints
data: list[list[int]] = parse_matrix(lines)

# part 1 solution
def part1() -> int:
    return sum(diffs)

print(f"result 1: {part1()}\n")

## part 2
# part 2 solution
def part2() -> int:
    return sum(sims)

print(f"result 2: {part2()}")













