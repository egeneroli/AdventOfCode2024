from typing import Tuple

import numpy as np

from py.util import AOCKata

# part 1 solution
class Part1(AOCKata):
    def __init__(self, test: bool = False, print_input: bool = True) -> None:
        # call parent constructor to read in data
        super().__init__(10, test, print_input)
        # parse data
        self.X: np.ndarray[int, int] = np.array([list(map(int, row)) for row in self.input_str.splitlines()])

    def on_grid(self, pos: tuple[int, int]) -> bool:
        # check if position is on the grid
        return (0 <= pos[0] < self.X.shape[0]) and (0 <= pos[1] < self.X.shape[1])

    def count(self, pos: tuple[int, int], starting_pos: tuple[int, int],
              trailheads: dict[tuple[int, int], int], visited: set[tuple[int, int]] = None) -> None:
        # call recursive method to traverse paths and count them if they reach completion
        # args: trailheads map, current position, trailhead started from,
        # if off grid, end/return
        if visited is None:
            visited = set()
        if not self.on_grid(pos):
            return
        # if at a peak(9), update map count for starting position, end/return
        if self.X[pos] == 9:
            if starting_pos not in trailheads:
                trailheads[starting_pos] = 0
            trailheads[starting_pos] += 1
            visited.clear()
            return

        # for each valid move from current position -- next postition must equal current position + 1
        for move in [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]:
            # check if move is valid
            if not self.on_grid(move) or move in visited:
                continue
            if self.X[move] == self.X[pos] + 1:
                # move to position and recurse
                # print(f"moving from {pos} to {move}")
                visited_temp: set[tuple[int, int]] = visited.copy()
                visited_temp.add(move)
                self.count(move, starting_pos, trailheads, visited_temp)

    def count2(self, data: np.ndarray[int, int], pos: tuple[int, int], END_CHAR: str = "9") -> int:
        # recursive method to traverse paths and count them if they reach completion
        # base case
        if data[pos] == END_CHAR:
            return 1

        # recursive case -- move in valid directions and count if path
        count: int = 0
        for move in [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]:
            # check if move is valid
            if self.on_grid(move) and data[move] == data[pos] + 1:
                count += self.count2(data, move)
        return count

    def run(self) -> int:
        X = self.X.copy()
        # parse input into grid
        print(X)
        # print(X.shape)
        # print(X[0][0])
        # print(X[(0,0)])

        # create empty map for trailhead positions and score (how many peaks can be reached from location)
        trailheads: dict[tuple[int, int], int] = {}

        # iterate over possible starting positions (zeros)
        indexes: list[tuple[int, int]] = list(zip(*np.nonzero(X == 0)))
        # visited: set[tuple[int, int]] = set()
        # indexes = [(int(pos[0]),int(pos[1])) for pos in indexes]
        print(indexes)
        for pos in indexes:
            # call recursive method to traverse paths and count them if they reach completion
            # self.count(pos, pos, trailheads)
            trailheads[pos] = self.count2(X, pos)

        print(trailheads)

        # return total trainhead score
        return sum(trailheads.values())

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













