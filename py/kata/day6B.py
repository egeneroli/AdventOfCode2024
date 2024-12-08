from py.util import read_input

# read in data
input_str: str = read_input("input6", False)

# parse data
mat: list[str] = input_str.split("\n")
# for row in mat:
#     print(row)

# part 1 solution
## globals
directions: tuple[str, ...] = ("^",">","v","<")

steps: list = [lambda pos: (pos[0]-1, pos[1], pos[2]),
               lambda pos: (pos[0], pos[1]+1, pos[2]),
               lambda pos: (pos[0]+1, pos[1], pos[2]),
               lambda pos: (pos[0], pos[1]-1, pos[2])]

import re
def get_pos() -> tuple[int, int, int]:
    # find position char and return position
    for x in range(len(mat)):
        row = mat[x]
        match = re.search(r"[\^>\v<]", row)
        if match:
            y: int = match.start()
            # print(f"x: {x}, y: {y}, char: {mat[x][y]}")
            return x, y, directions.index(match.group())

def turn_right(dir_index: int) -> int:
    # turn 90 degress to right
    return (dir_index + 1) % len(directions)

def on_grid(pos: tuple[int, int, int]) -> bool:
    # determines if a position is on/off the grid
    return (0 <= pos[0] < len(mat)) and (0 <= pos[1] < len(mat[0]))

class OffGrid(Exception):
    # class for OffGridException
    pass

def mark(x: int, y: int, marker: str) -> None:
    mat[x] = mat[x][:y] + marker + mat[x][y+1:]

def move(pos: tuple[int, int, int]) -> tuple[int, int, int]:
    # try to move forward in direction already facing
    # get candidate position
    new_pos: tuple[int, int, int] = steps[pos[2]](pos)
    x, y, dir = pos
    x_new, y_new, _ = new_pos

    # check if OB -- raise exception
    if not on_grid(new_pos):
        raise OffGrid("Out of bounds")

    # check if it is an obstacle
    if "#" == mat[x_new][y_new]:
        # if so, turn right
        new_pos = (x, y, turn_right(dir))
    # if not, accept new position
    else:
        # mark old position
        mark(x, y, "X")

        # mark current position
        mark(x_new, y_new, directions[dir])

    return new_pos

def patrol():
    # iteratively step while still in bounds
    # while on grid, move -- if OB, end
    pos: tuple[int, int, int] = get_pos()
    # print(f"pos: {pos}")
    while True:
        try:
            pos = move(pos)
            # print(f"pos: {pos}")
        except OffGrid:
            break

def part1() -> int:
    # patrol by iterating guard "walk"
    patrol()
    # count all visited spaces, add one for last position
    return sum(line.count("X") for line in mat) + 1

print(f"result 1: {part1()}\n")
# for row in mat:
#     print(row)

## part 2
# part 2 solution
def part2() -> int:
    return -1

print(f"result 2: {part2()}")













