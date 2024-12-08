from py.util import read_input
import numpy as np

# read in data
input_str: str = read_input("input8")

# part 1 solution
class Part1:
    def __init__(self) -> None:
        # parse data
        self.mat: np.ndarray[str, str] = np.array([list(row) for row in input_str.strip().split("\n")])

    def extrapolate(self, pos1: tuple[int, int], pos2: tuple[int, int]) -> list[tuple[int, int]]:
        # calculate slope / delta
        d: tuple[int, int] = (pos2[0] - pos1[0], pos2[1] - pos1[1])
        # calculate next position from each point
        positions: list[tuple[int, int]] = [(pos1[0] - d[0], pos1[1] - d[1]), (pos2[0] + d[0], pos2[1] + d[1])]
        return [pos for pos in positions if self.in_bounds(pos)]

    def get_indexes(self, char: str) -> list[tuple[int, int]]:
        return [(int(i), int(j)) for i, j in zip(*np.nonzero(self.mat == char))]

    def in_bounds(self, pos: tuple[int, int]) -> bool:
        return 0 <= pos[0] < len(self.mat) and 0 <= pos[1] < len(self.mat[0])

    def get_antinodes(self, antennas: list[tuple[int, int]]) -> list[tuple[int, int]]:
        # iterate over all pairs of positions
        antinodes: list[tuple[int, int]] = []
        for i in range(len(antennas)):
            for j in range(i+1, len(antennas)):
                # extrapolate antinode locations from pair
                locs: list[tuple[int, int]] = self.extrapolate(antennas[i], antennas[j])
                if locs:
                    antinodes.extend(locs)
                # if on board, add to results
                # for pos in locs:
                #     if self.in_bounds(pos):
                #         antinodes.append(pos)

        return antinodes

    def get_all_unique_antinodes(self) -> set[tuple[int, int]]:
        # iterate over every position in array
            # if char at position is not '.'
                # if "frequency" (char) not already evaluated
                    # find all antinodes created by frequency
                    # -- get all positions with given frequency
                    # -- iterate over all pairs of positions
                        # calculate slope
                        # calculate next position
                        # if OB, throw away
                        # if valid, count

        checked_freqs: set[str] = set()
        antinodes: set[tuple[int, int]] = set()

        # loop over each char in array
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                # make sure this is an antenna and not empty spot (.)
                if self.mat[i][j] != ".":
                    freq: str = self.mat[i][j]
                    # if char not already evaluated
                    if freq not in checked_freqs:
                        # find all antennas with frequency (indices with same char)
                        positions: list[tuple[int, int]] = self.get_indexes(freq)
                        # print(f"positions: {positions}")

                        # find all antinodes created by frequency
                        anodes: list[tuple[int, int]] = self.get_antinodes(positions)
                        # print(f"antinodes for freq '{freq}': {anodes}\n")

                        # add antinodes to set of all antinodes
                        antinodes.update(anodes)

                        # add frequency char to set/list to mark as evaluated
                        checked_freqs.add(freq)

        return antinodes

    def run(self) -> int:
        return len(self.get_all_unique_antinodes())

def part1() -> int:
    return Part1().run()

print(f"result 1: {part1()}\n")

## part 2
# part 2 solution
class Part2(Part1):
    def extrapolate(self, pos1: tuple[int, int], pos2: tuple[int, int]) -> list[tuple[int, int]]:
        # print(f"\npos1: {pos1}, pos2: {pos2}, anntenna: {self.mat[pos1]}")
        # calculate slope / delta
        y1, x1 = pos1
        y2, x2 = pos2
        m: float = (y2 - y1) / (x2 - x1)
        # print(f"x1: {x1}, y1: {y1}; x2: {x2}, y2: {y2}")
        # print(f"m: {m}")

        # use slope to iteratively calculate possible positions and then validate
        # positions: set[tuple[int, int]] = set()
        positions: list[tuple[int, int]] = []
        # iterate over x values
        for x in range(0, int(self.mat.shape[1])):
            # calculate y value for given x from slope
            y: float = m * (x - x1) + y1
            # print(f"x: {x}, y: {y}")
            pos: tuple[int, int] = (int(y), x)
            # if valid position, add to set
            if y.is_integer() and self.in_bounds(pos):
                # print(f"valid position: {pos}")
                positions.append(pos)
        return positions

        # # calculate next position from each point
        # positions: list[tuple[int, int]] = [(pos1[0] - d[0], pos1[1] - d[1]), (pos2[0] + d[0], pos2[1] + d[1])]
        # return [pos for pos in positions if self.in_bounds(pos)]

    def run(self) -> int:
        antinodes: set[tuple[int, int]] = self.get_all_unique_antinodes()
        mat_temp: np.ndarray[str, str] = self.mat.copy()
        for pos in antinodes:
            mat_temp[pos] = "#"
        for row in mat_temp:
            print("".join(row))
        return len(antinodes)

def part2() -> int:
    return Part2().run()

print(f"result 2: {part2()}\n")













