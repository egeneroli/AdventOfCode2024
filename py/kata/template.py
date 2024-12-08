from py.util import read_input

# read in data
input_str: str = read_input("input3")

# part 1 solution
class Part1:
    def __init__(self) -> None:
        # parse data
        self.mat: list[list[str]] = [list(row) for row in input_str.strip().split("\n")]

    def run(self) -> int:
        return -1

def part1() -> int:
    return Part1().run()

print(f"result 1: {part1()}\n")


## part 2
class Part2(Part1):

    def run(self) -> int:
        return -1

def part2() -> int:
    return Part2().run()

print(f"result 2: {part2()}\n")













