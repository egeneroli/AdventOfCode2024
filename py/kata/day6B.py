from py.util import read_input

# read in data
input_str: str = read_input("input6test", False)

# parse data
mat: list[str] = input_str.split("\n")
# for row in mat:
#     print(row)

# part 1 solution
## globals
directions: tuple[str, ...] = ("^",">","v","<")

steps: list = [lambda pos: (pos[0]-1, pos[1]),
               lambda pos: (pos[0], pos[1]+1),
               lambda pos: (pos[0]+1, pos[1]),
               lambda pos: (pos[0], pos[1]-1)]

def step(pos: tuple[int, int, int]) -> tuple[int, int, int]:
    # step in current direction
    x, y, dir = pos
    x, y = steps[dir]((x, y))
    return x, y, dir

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

def get_char(x: int, y: int) -> str:
    return mat[x][y]

def move(pos: tuple[int, int, int]) -> tuple[int, int, int]:
    # try to move forward in direction already facing
    # get candidate position
    new_pos: tuple[int, int, int] = step(pos)
    x, y, dir = pos
    x_new, y_new, _ = new_pos

    # check if OB -- raise exception
    if not on_grid(new_pos):
        raise OffGrid("Out of bounds")

    # check if it is an obstacle
    if "#" == get_char(*new_pos[:2]):
    # while "#" == mat[x_new][y_new]:
        # if so, turn right
        new_pos = (*pos[:2], turn_right(dir))

    # if not, accept new position
    # else:
    # mark old position
    mark(*pos[:2], "X")

    # mark current position
    mark(*new_pos[:2], directions[pos[2]])

    return new_pos

def part1():
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
    return sum(line.count("X") for line in mat) + 1

print(f"result 1: {part1()}\n")
for row in mat:
    print(row)

## part 2
# part 2 solution
def part2() -> int:
    return -1

print(f"result 2: {part2()}")













