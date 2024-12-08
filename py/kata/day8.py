from py.util import read_input
import numpy as np

# read in data
input_str: str = read_input("input8test")

# parse data
mat: np.ndarray[str, str] = np.array([list(row) for row in input_str.strip().split("\n")])

# part 1 solution
def extrapolate(pos: tuple[int, int], pos2: tuple[int, int]) -> tuple[int, int]:
    # calculate slope / delta
    d: tuple[int, int] = (pos2[0] - pos[0], pos2[1] - pos[1])
    # calculate next position
    return (pos2[0] + d[0]), (pos2[1] + d[1])

def get_indexes(char: str) -> list[tuple[int, int]]:
    return [(int(i), int(j)) for i, j in zip(*np.nonzero(mat == char))]

def in_bounds(pos: tuple[int, int]) -> bool:
    return 0 <= pos[0] < len(mat) and 0 <= pos[1] < len(mat[0])

def get_antinodes(antennas: list[tuple[int, int]]) -> list[tuple[int, int]]:
    # iterate over all pairs of positions
    antinodes: list[tuple[int, int]] = []
    for i in range(len(antennas)):
        for j in range(0, len(antennas)):
            if i != j:
                # extrapolate next position -- if on board, add to results
                pos: tuple[int, int] = extrapolate(antennas[i], antennas[j])
                if in_bounds(pos):
                    antinodes.append(pos)
    return antinodes

def part1() -> int:
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
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            # make sure this is an antenna and not empty spot (.)
            if mat[i][j] != ".":
                freq: str = mat[i][j]
                # if char not already evaluated
                if freq not in checked_freqs:
                    # find all antennas with frequency (indices with same char)
                    # positions: list[tuple[int, int]] = [(int(i), int(j)) for i, j in zip(*np.nonzero(mat == freq))]
                    positions: list[tuple[int, int]] = get_indexes(freq)
                    print(f"positions: {positions}")
                    print([str(mat[pos]) for pos in positions])

                    # find all antinodes created by frequency
                    anodes: list[tuple[int, int]] = get_antinodes(positions)
                    print(f"antinodes for freq {freq}: {anodes}")

                    # add antinodes to set of all antinodes
                    antinodes.update(anodes)

                    # add frequency char to set/list to mark as evaluated
                    checked_freqs.add(freq)

                    print()

    return len(antinodes)

print(f"result 1: {part1()}\n")

## part 2
# part 2 solution
def part2() -> int:
    return -1

print(f"result 2: {part2()}")













