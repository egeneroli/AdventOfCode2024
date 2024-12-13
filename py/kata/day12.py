from itertools import count

import numpy as np

from py.util import AOCKata

# part 1 solution
class Part1(AOCKata):
    def __init__(self, test: bool = False, print_input: bool = True) -> None:
        # call parent constructor to read in data
        super().__init__(12, test, print_input)
        # parse data
        self.X: np.ndarray[str, str] = np.array([list(row) for row in self.input_str.splitlines()])

    def has_shared_edge(self, pos1: tuple[int, int], pos2: tuple[int, int]) -> bool:
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) == 1

    def is_connected(self, pos1: tuple[int, int], indexes: list[tuple[int, int]]) -> bool:
        for pos2 in indexes:
            if self.has_shared_edge(pos1, pos2):
                return True
        return False

    def count_shared_edges(self, indexes: list[tuple[int, int]]) -> int:
        # for each pair of indexes
        count: int = 0
        for i in range(len(indexes)):
            for j in range(i+1, len(indexes)):
                # count if indexes are adjacent
                if self.has_shared_edge(indexes[i], indexes[j]) == 1:
                    count += 1
        return count

    def get_region_price(self, indexes: list[tuple[int, int]]) -> int:
        # calculate shared edges
        shared_edges: int = self.count_shared_edges(indexes)
        # calculate area
        area: int = len(indexes)
        # calculate perimeter = area * 4 - shared edges * 2
        perimeter: int = area * 4 - shared_edges * 2
        # calc price for region = perimeter * area (number of spaces)
        price: int = perimeter * area
        return price

    def on_grid(self, pos: tuple[int, int]) -> bool:
        # check if position is on the grid
        return (0 <= pos[0] < self.X.shape[0]) and (0 <= pos[1] < self.X.shape[1])

    def get_regions(self, X: np.ndarray[str, str]) -> list[list[tuple[int, int]]]:
        # get all the contiguous regions recursively
        regions: list[list[tuple[int, int]]] = []
        visited: np.ndarray[bool, bool] = np.zeros(X.shape, dtype=bool)
        # self.search(X, regions)
        # for each position -- search neighbors recursively if not visited
        for i in range(len(X)):
            for j in range(len(X[0])):
                region: list[tuple[int, int]] = []
                # search all valid neighbors and add to region
                self.search((i, j), region, visited)
                if region:
                    regions.append(region)

        return regions

    def search(self, pos: tuple[int, int], region: list[tuple[int, int]], visited: np.ndarray[bool, bool]) -> None:
        # get regions recursively -- search all valid neighbors
        # base case / exit condition(s) -- if visited end, else mark visited
        if visited[pos]:
            return
        visited[pos] = True

        # recursive step
        region.append(pos) # add current position to region
        # move in each direction if valid move and same value at position
        for move in [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]:
            if self.on_grid(move) and self.X[move] == self.X[pos]:
                self.search(move, region, visited)

    def run(self) -> int:
        # parse input into grid of chars (str)
        X: np.ndarray[str, str] = self.X.copy()
        print(X)
        print(f"shape: {X.shape}")

        # get list of regions
        regions: list[list[tuple[int, int]]] = self.get_regions(X)
        # print(regions)

        # for each value
        count: int = 0
        for region in regions:
            # print(f"{self.X[region[0]]}: {len(region)} -- {region}")
        #     # get region price
            price: int = self.get_region_price(region)
            count += (price)
            print(f"{self.X[region[0]]}: {len(region)}, price: {price}, total price: {count}")
        return count

def part1() -> int:
    return Part1(test=False, print_input=False).run()

# print(f"result 1: {part1()}\n")


## part 2
class Part2(Part1):

    def get_region_price(self, region: list[tuple[int, int]]) -> int:
        # for part 2, region price = area * sides
        # calculate area
        area: int = len(region)
        # calculate sides = area * 4
        sides: int = self.count_sides(region)
        # calc price for region = sides *
        price: int = sides * area
        return price

    def count_sides(self, region: list[tuple[int, int]]) -> int:
        # count sides of a region
        pass

    def count_total_sides(self, X: np.ndarray[str, str]) -> list[list[tuple[int, int]]]:
        # get all the contiguous regions recursively
        regions: list[list[tuple[int, int]]] = []
        visited: np.ndarray[bool, bool] = np.zeros(X.shape, dtype=bool)
        # self.search(X, regions)
        # for each position -- search neighbors recursively if not visited
        count: int = 0
        for i in range(len(X)):
            for j in range(len(X[0])):
                # search all valid neighbors and add price of region
                n_visited: int = visited.sum()
                sides: int = self.count((i, j), visited)
                area: int = visited.sum() - n_visited
                count += sides * area
                print(f"pos: ({i},{j}), sides: {sides}, area: {area}, count: {count}")
        return count

    def count(self, pos: tuple[int, int], visited: np.ndarray[bool, bool]) -> int:
        # sides of region recursively -- search all valid neighbors
        # base case / exit condition(s) -- if visited end, else mark visited
        if visited[pos]:
            return 1
        visited[pos] = True

        # recursive step
        count: int = 0
        # move in each direction if valid move and same value at position
        for move in [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]:
            if not self.on_grid(move) or self.X[move] != self.X[pos]:
                # print(f"move: {move}, visited: {visited}")
                count += 1
            else:
                count += self.count(move, visited)
        return count

    def run(self) -> int:
        return self.count_total_sides(self.X)

def part2() -> int:
    return Part2(test=True, print_input=False).run()

print(f"result 2: {part2()}\n")













