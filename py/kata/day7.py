from py.util import read_input
from itertools import product

# read in data
input_str: str = read_input("input7", False)

# parse data
lines: list[str] = input_str.split("\n")

# part 1 solution
# define globals
operators: tuple = (lambda x, y: x + y, lambda x, y: x * y, lambda x, y: int(str(x)+str(y)))

def is_valid(nums: list[int], target: int, ops: tuple = operators[:2]) -> bool:
    # recursive function to check all possible combinations of operators and num pairs
    # end condition(s)
    if nums[0] > target:
        return False
    if len(nums) == 1:
        return target == nums[0]
    # recursive case(s)
    for op in ops:
        # apply operator, update nums
        nums_new: list[int] = [op(nums[0], nums[1])] + nums[2:]
        # check if result is target
        if is_valid(nums_new, target, ops):
            return True
    # no valid result
    return False

def count_total_score(ops: tuple) -> int:
    # loop over each line
    # check if number can be produced by any combination of operators
    count: int = 0
    for line in lines:
        target: int = int(line.split(":")[0])
        nums: list[int] = [int(num) for num in line.split(":")[1].split()]
        if is_valid(nums, target, ops):
            # print(f"target: {target}, nums: {nums}")
            count += target

    return count

def part1() -> int:
    return count_total_score(operators[:2])
p1_score: int = part1()
print(f"result 1: {part1()}\n")

## part 2
# part 2 solution
def part2() -> int:
    return count_total_score(operators)

print(f"result 2: {part2()}")













