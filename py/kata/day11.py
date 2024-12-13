from py.util import AOCKata

from functools import lru_cache

# part 1 solution
class Part1(AOCKata):
    def __init__(self, test: bool = False, print_input: bool = True) -> None:
        # call parent constructor to read in data
        super().__init__(11, test, print_input)
        # parse data
        # self.mat: list[list[str]] = [list(row) for row in self.input_str.strip().split("\n")]

    def count(self, stones: list[int], n: int) -> int:
        print(f"n = {n}")
        # recursive method to count all stones
        # base cases
        if n == 0:
            return len(stones)

        lst: list[int] = []
        for x in stones:
            # print(f"i: {i}, x: {x}")
            # if 0, -> 1
            if x == 0:
                lst.append(1)
            # if num has even number of digits, split in two
            elif len(str(x)) % 2 == 0 and x > 9:
                s: str = str(x)
                n_2: int = len(s) // 2
                # print(f"s: {s}, n: {n}")
                lst.extend([int(s[:n_2]), int(s[n_2:])])
            else:
                # multiply by 2024 if nothing else
                lst.append(x*2024)
            # print(lst)
        return self.count(lst, n-1)

    def run(self) -> int:
        stones: list[int] = list(map(int, self.input_str.split()))
        return self.count(stones, 25)


def part1() -> int:
    return Part1(test=False, print_input=True).run()

# print(f"result 1: {part1()}\n")


## part 2
class Part2(Part1):

    @lru_cache(None)
    def count_recursive(self, x: int, n: int) -> int:
        # recursive method to count all stones

        # base cases
        if n == 0:
            return 1

        if x == 0:  # if 0, -> 1
            return self.count_recursive(1, n-1)
        elif len(str(x)) % 2 == 0 and x > 9:  # if num has even number of digits, split in two -- count
            s: str = str(x)
            n_2: int = len(s) // 2
            # print(f"s: {s}, n: {n}")
            return self.count_recursive(int(s[:n_2]), n-1) + self.count_recursive(int(s[n_2:]), n-1)
        else:  # multiply by 2024 if nothing else
            return self.count_recursive(x*2024, n-1)

    def count(self, stones: list[int], n: int) -> int:
        return sum(self.count_recursive(stone, n) for stone in stones)

    def run(self) -> int:
        stones: list[int] = list(map(int, self.input_str.split()))
        return self.count(stones, 75)


def part2() -> int:
    return Part2(test=False, print_input=True).run()

print(f"result 2: {part2()}\n")













