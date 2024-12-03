from time import monotonic

from py.util import read_input, parse_matrix

# read in data
lines: list[str] = read_input("input2test")
print(f"input: {lines[0:10]}\n")

# parse into nested list of ints
data: list[list[int]] = parse_matrix(lines)

# part 1 solution
def monotonic_diffs(diffs: list[int]) -> bool:
    return all(diff < 0 for diff in diffs) or all(diff > 0 for diff in diffs)

def correct_size_diffs(diffs: list[int]) -> bool:
    return all(abs(diff) in [1,2,3] for diff in diffs)

def safe_row(row: list[int]) -> bool:
    # calculate differences
    diffs: list[int] = [row[i + 1] - row[i] for i in range(0, len(row) - 1)]
    print(f"diffs: {diffs}")
    mono: bool = monotonic_diffs(diffs)
    print(f"mono: {mono}")
    correct_size: bool = correct_size_diffs(diffs)
    print(f"correct size: {correct_size}")
    print(f"safe: {mono and correct_size}\n")
    return mono and correct_size

def part1() -> int:
    return sum(safe_row(row) for row in data)

print(f"result 1: {part1()}\n")

## part 2
# part 2 solution
def almost_safe_row(row: list[int]) -> bool:
    diffs: list[int] = [row[i + 1] - row[i] for i in range(0, len(row) - 1)]
    print(f"diffs: {diffs}")

    # check that only one diff is wrong
    sum(diff < 0 for diff in diffs) or sum(diff > 0 for diff in diffs)


def part2() -> int:
    return sum(sims)

print(f"result 2: {part2()}")













