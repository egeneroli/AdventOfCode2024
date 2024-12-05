from py.util import read_input, parse_int_matrix

# read in data
input_str: str = read_input("input5", print_input=False)

# parse data
orders_str: list[str] = input_str.split("\n\n")[0].split("\n")
# print(f"order: {orders}")
orders: list[tuple[int, int]] = [(int(x), int(y)) for x, y in [order.split("|") for order in orders_str]]
# print(f"order: {orders}")

updates_str: list[str] = input_str.split("\n\n")[1].split("\n")
# print(f"updates: {updates}")
updates: list[list[int]] = [[int(x) for x in update.split(",")] for update in updates_str]
# print(f"updates: {updates}")

# part 1 solution
def correct_order(pages: list[int], order: list[tuple[int, int]]) -> bool:
    # check if page list is in correct order
    for i in range(len(pages)-1):
        page: int = pages[i]
        next: int = pages[i+1]
        # loop over all order rules
        for rule in order:
            # if rule contains page and next in wrong order (next, page), return False
            if page == rule[1] and next == rule[0]:
                return False

    return True

def part1() -> int:
    # get correct ordered updates
    correct_updates = [update for update in updates if correct_order(update, orders)]
    # print(f"correct updates: {correct_updates}")

    # calculate final result
    # print([update[int(update.__len__()/2)] for update in correct_updates])
    return sum(update[int(update.__len__()/2)] for update in correct_updates)

print(f"result 1: {part1()}\n")

## part 2
# part 2 solution
from functools import cmp_to_key

def order_comparator(a: int, b: int) -> int:
    # get pair containing a and b (should only be one)
    for pair in set(pair for pair in orders if a in pair and b in pair):
        # return difference between indices
        return pair.index(a) - pair.index(b)

    # if no match, return 0
    return 0

def part2() -> int:
    # get incorrect ordered updates
    incorrect_updates = [update for update in updates if not correct_order(update, orders)]
    # print(f"incorrect updates: {incorrect_updates}")

    # order incorrect updates
    corrected_updates: list[list[int]] = [sorted(update, key=cmp_to_key(order_comparator)) for update in incorrect_updates]
    # print(f"corrected updates: {corrected_updates}")

    return sum(update[int(update.__len__()/2)] for update in corrected_updates)

print(f"result 2: {part2()}")













