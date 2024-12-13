import re

import numpy as np

from py.util import AOCKata

# part 1 solution
class Part1(AOCKata):
    def __init__(self, test: bool = False, print_input: bool = True) -> None:
        # call parent constructor to read in data
        super().__init__(13, test, print_input)
        # parse data

    def parse_data(self) -> list[dict[str, tuple[int, int]]]:
        results: list[dict[str, tuple[int, int]]] = []
        # iterate over blocks
        for block in self.input_str.split("\n\n"):
            # iterate over lines
            machine: dict[str, tuple[int, int]] = {}
            for line in block.split("\n"):
                # get key
                key: str = line.split(": ")[0].split()[-1]
                # get value
                value: tuple[int, int] = tuple(map(int, re.findall("\d+", line.split(": ")[1])))
                # add to map
                machine[key] = value
            # add machine map to results
            results.append(machine)
        return results

    def solve_machine(self, a: tuple[int, int], b: tuple[int, int], p: tuple[int, int]) -> tuple[int, int]:
        # use linear algebra to solve system of equations
        xy: np.ndarray[int, int] = np.array([[a[0], b[0]], [a[1], b[1]]])
        p: np.ndarray[int, int] = np.array([p[0], p[1]])
        return tuple(np.linalg.solve(xy, p))

    def run(self) -> int:
        # parse data
        # break up blocks by \n\n
        # parse block into map -- ex. A: (20,17), B: (37, 14), Prize: (2036, 9820)
        # add to overall list
        machines: list[dict[str, tuple[int, int]]] = self.parse_data()
        print(machines)

        # process each machine
            # determine solution to system of equations

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

# print(f"result 2: {part2()}\n")













