from py.util import read_input, parse_int_matrix

# read in data
input_str: str = read_input("input2")

# parse into nested list of ints
data: list[list[int]] = parse_int_matrix(input_str.split("\n"))

# part 1 solution
def monotonic_diffs(diffs: list[int]) -> bool:
    return all(diff < 0 for diff in diffs) or all(diff > 0 for diff in diffs)

def correct_size_diffs(diffs: list[int]) -> bool:
    return all(abs(diff) in [1,2,3] for diff in diffs)

def safe_row(row: list[int]) -> bool:
    # calculate differences
    diffs: list[int] = [row[i + 1] - row[i] for i in range(0, len(row) - 1)]
    #print(f"diffs: {diffs}")
    # check if all positive or all negative
    mono: bool = monotonic_diffs(diffs)
    #print(f"mono: {mono}")
    # check if all differences are in range
    correct_size: bool = correct_size_diffs(diffs)
    #print(f"correct size: {correct_size}")
    #print(f"safe: {mono and correct_size}\n")
    return mono and correct_size

def part1() -> int:
    return sum(safe_row(row) for row in data)

print(f"result 1: {part1()}\n")


## part 2
# part 2 solution
def safe_row2(row: list[int]) -> bool:
    # if completely safe, return True
    if safe_row(row):
        return True

    # check if almost safe (ie. only one level is unsafe)
    for i, level in enumerate(row):
        # create a copy of the level
        level_temp: list[int] = row.copy()
        # remove the level
        level_temp.pop(i)
        # check if the copy is safe
        if safe_row(level_temp):
            return True

    # if not, return False
    return False

def part2() -> int:
    return sum(safe_row2(row) for row in data)

print(f"result 2: {part2()}")













