from py.util import AOCKata

# part 1 solution
class Part1(AOCKata):
    def __init__(self, test: bool = False, print_input: bool = True) -> None:
        # call parent constructor to read in data
        super().__init__(11, test, print_input)
        # parse data
        # self.mat: list[list[str]] = [list(row) for row in self.input_str.strip().split("\n")]

    def blink(self, stones: list[int]) -> list[int]:
        lst: list[int] = []
        for i, x in enumerate(stones):
            # print(f"i: {i}, x: {x}")
            # if 0, -> 1
            if x == 0:
                lst.append(1)
            # if num has even number of digits, split in two
            elif len(str(x)) % 2 == 0 and x > 9:
                s: str = str(x)
                n: int = len(s) // 2
                # print(f"s: {s}, n: {n}")
                lst.extend([int(s[:n]), int(s[n:])])
            else:
                # multiply by 2024 if nothing else
                lst.append(x*2024)
            # print(lst)
        return lst

    def blink2(self, stones: list[int]) -> int:
        count: int = 0
        for i, x in enumerate(stones):
            # print(f"i: {i}, x: {x}")
            # if 0, -> 1
            ###### use recursion to pass through the counts and how the are groing from evens
            if len(str(x)) % 2 == 0 and x > 9:
                count += 2
            else:
                count += 1
            # print(lst)
        return count

    def count(self, n: int, stones: list[int]) -> int:
        # parse data into list of ints (stones)
        stones: list[int] = stones
        # print(stones)

        for _ in range(n):
            stones = self.blink(stones)
            print(f"i: {_}, n: {len(stones)}")

        return len(stones)

    def run(self):
        stones: list[int] = list(map(int, self.input_str.split()))
        return self.count(25, stones)


def part1() -> int:
    return Part1(test=False, print_input=True).run()

# print(f"result 1: {part1()}\n")


## part 2
class Part2(Part1):

    def count(self, n: int) -> int:
        # recursive method to count all stones


    def run(self) -> int:
        return self.count(75)

def part2() -> int:
    return Part2(test=False, print_input=True).run()

print(f"result 2: {part2()}\n")













