from py.util import read_input

# read in data
lines: list[str] = read_input("input1")
# print(lines[0:10])

# parse data
def parse_data(x: list[str]) -> list[list[int]]:
    return [[int(x) for x in line.split()] for line in x]

data: list[list[int]] = parse_data(lines)
# print(data[0:10])

# calculate differences
def calc_diffs(x: list[list[int]]) -> list[int]:
    list1: list[int] = [x[0] for x in x]
    list1.sort()
    list2: list[int] = [x[1] for x in x]
    list2.sort()
    return [abs(x1 - x2) for x1, x2 in zip(list1, list2)]

diffs: list[int] = calc_diffs(data)
# print(diffs[0:10])

print(f"result: {sum(diffs)}")













