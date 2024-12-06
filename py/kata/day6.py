from py.util import read_input
import numpy as np

# read in data
input_str: str = read_input("input6")

# parse data
data_raw: np.ndarray[str, str] = np.array([list(row) for row in input_str.strip().split("\n")])
data: np.ndarray[str, str] = data_raw

# part 1 solution
# find starting position and direction
directions: list[str] = ["^", ">", "v", "<"]
pos: tuple[int, int] = tuple([x[0] for x in np.where(np.isin(data, directions))])
dir: str = data[pos]
dir_index: int = directions.index(dir)

# iterate "walking" until guard has left area
step: list = [lambda pos: (pos[0]-1, pos[1]), lambda pos: (pos[0], pos[1]+1), lambda pos: (pos[0]+1, pos[1]), lambda pos: (pos[0], pos[1]-1)]

def walk():
    # If there is something directly in front of you, turn right 90 degrees.
    # Otherwise, take a step forward.
    # ^ -> row--, > -> col++, v -> row++, < -> col--
    # attempt to move forward
    global pos, dir_index, data
    new_pos: tuple[int, int] = step[dir_index](pos)

    # try to move, data[new_pos] might be out of bounds
    try:
        # mark position as visited
        data[pos] = "x"
        # if blocked, turn right
        if data[new_pos] == "#":
            # update direction
            dir_index = (dir_index + 1) % 4
            # set new position to original position
            new_pos = pos
        # mark new position with current direction
        data[new_pos] = directions[dir_index]
    except IndexError:
        pass
    finally:
        pos = new_pos

def part1() -> int:
    global pos, dir_index, data
    while -1 < pos[0] < data.shape[0] and -1 < pos[1] < data.shape[1]:
        walk()
    return np.count_nonzero(data == "x")

print(f"result 1: {part1()}\n")

## part 2

# find starting position and direction
# directions: list[str] = ["^", ">", "v", "<"]
#
# start_pos: tuple[int, int] = tuple([x[0] for x in np.where(np.isin(data, directions))])
#
# def part2() -> int:
#     # iterate through each starting point
#     valid_pos_count: int = 0
#     for row in range(data.shape[0]):
#         for col in range(data.shape[1]):
#             retrace_count: int = 0
#             data = data_raw
#             data[row][col] = "#"
#             pos: tuple[int, int] = start_pos
#             dir: str = data[pos]
#             dir_index: int = directions.index(dir)
#             while -1 < pos[0] < data.shape[0] and -1 < pos[1] < data.shape[1] and retrace_count < 10:
#                 print(f"pos: {pos}, dir: {dir}, retrace count: {retrace_count}")
#                 if data[pos] == "x":
#                     retrace_count += 1
#                 else:
#                     retrace_count = 0
#                 walk()
#             print(f"retrace count: {retrace_count}")
#             if retrace_count == 10:
#                 valid_pos_count += 1
#     return valid_pos_count

# print(f"result 2: {part2()}")













