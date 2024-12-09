from py.util import AOCKata

# part 1 solution
class Part1(AOCKata):
    def __init__(self, test: bool = False, print_input: bool = True) -> None:
        # call parent constructor to read in data
        super().__init__(9, test, print_input)
        # parse data
        self.disk_map: list[int] = [int(x) for x in list(self.input_str)]
        print(f"data: {self.disk_map}")

    def run(self) -> int:
        return -1

def part1() -> int:
    return Part1(test=True, print_input=True).run()

print(f"result 1: {part1()}\n")


## part 2
class Part2(Part1):

    def run(self) -> int:
        return -1

def part2() -> int:
    return Part2().run()

print(f"result 2: {part2()}\n")













