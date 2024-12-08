from operator import index

from py.util import read_input
import numpy as np

# read in data
input_str: str = read_input("input6", False)

# parse data
data_parsed: np.ndarray[str, str] = np.array([list(row) for row in input_str.strip().split("\n")])

# define global variables
VISITED: str = "X"
# VISITED_PATTERN: str = r"X"
OBSTACLE: str = "#"
# OBSTACLE_PATTERN: str = r"\#"
directions: list[str] = ["^", ">", "v", "<"]
start_pos: tuple[int, int] = tuple([x[0] for x in np.where(np.isin(data_parsed, directions))])
start_dir_index: int = directions.index(data_parsed[start_pos])
# ^ -> row--, > -> col++, v -> row++, < -> col--
step: list = [lambda pos: (pos[0]-1, pos[1]), lambda pos: (pos[0], pos[1]+1), lambda pos: (pos[0]+1, pos[1]), lambda pos: (pos[0], pos[1]-1)]

## part 1
import re
def is_visited(char: str) -> bool:
    # return bool(re.match(VISITED_PATTERN, str(char)))
    return char == VISITED

def mark_visited(x: np.ndarray[str, str], pos: tuple[int, int]) -> None:
    x[pos] = VISITED

def is_obstacle(char: str) -> bool:
    # return bool(re.match(OBSTACLE_PATTERN, str(char)))
    return char == OBSTACLE

def increment_dir(dir_index: int) -> int:
    return (dir_index + 1) % 4

def walk(x: np.ndarray[str, str], pos: tuple[int, int], dir: int) -> (int, int):
    # If there is something directly in front of you, turn right 90 degrees. Otherwise, take a step forward.
    new_pos: tuple[int, int] = step[dir](pos)
    # print(f"pos: {pos}, new_pos: {new_pos}, dir: {dir}")
    # print(x)

    try: # try to move forward (new_pos might be off the board)
        # mark position as visited
        mark_visited(x, pos)
        # if blocked, turn right
        if is_obstacle(x[new_pos]):
            # update direction
            dir = increment_dir(dir)
            # set new position to original position
            new_pos = pos
        # mark new position with current direction
        x[new_pos] = directions[dir]
    except IndexError:
        pass
    return new_pos, dir

def in_bounds(x: np.ndarray[str, str], pos: tuple[int, int]) -> bool:
    return -1 < pos[0] < x.shape[0] and -1 < pos[1] < x.shape[1]

def print_board(x: np.ndarray[str, str]):
    for row in x:
        print("".join(row))

class InfineteLoopError(Exception):
    # exception for infinite loop
    pass

def patrol(x: np.ndarray[str, str], pos: tuple[int, int] = start_pos, dir: int = start_dir_index) -> int:
    # find starting position and direction
    visited: set[tuple[tuple[int, int], str]] = set()
    while in_bounds(x, pos):
        pos, dir = walk(x, pos, dir)
        if (pos, dir) in visited:
            # print(f"loop detected at {pos}, {dir}")
            # print(visited)
            raise InfineteLoopError("loop detected")
        visited.add((pos, dir))
    return np.sum(np.vectorize(is_visited)(x))

def part1(x: np.ndarray[str, str]) -> int:
    return patrol(x)

data: np.ndarray[str, str] = data_parsed.copy()
# part1(data)
print(f"result 1: {part1(data)}\n")
# print_board(data)

## part 2
def is_loop(x: np.ndarray[str, str], pos: tuple[int, int], dir: int) -> bool:
    # visited: set[tuple[tuple[int, int], str]] = set()
    # while in_bounds(x, pos):
    #     pos, dir = walk(x, pos, dir)
    #     if (pos, dir) in visited:
    #         return True
    #     visited.add((pos, directions[dir]))
    # return False
    try:
        patrol(x, pos, dir)
    except InfineteLoopError:
        return True
    return False

def valid_obstacle_pos(x: np.ndarray[str, str], pos: tuple[int, int], dir: int) -> bool:
    x_temp: np.ndarray[str, str] = x.copy()
    x_temp[pos] = OBSTACLE
    return is_loop(x_temp, pos, dir)

def part2(x: np.ndarray[str, str], pos: tuple[int, int] = start_pos, dir: int = start_dir_index) -> int:
    valid_pos_count: int = 0
    x[pos] = "."
    for tup in np.argwhere(data == 'X'):
        tup = tuple(int(x) for x in tup)
        # print(f"pos: {tuple(int(x) for x in tup)}")
    # while in_bounds(x, pos):
    #     # while in bounds, patrol/walk like before
    #     pos, dir = walk(x, pos, dir)
        # try:
        #     x_temp: np.ndarray[str, str] = x.copy()
        #     x_temp[step[dir](pos)] = OBSTACLE

        # after each step, check if putting obstacle in front of guard results in loop
        # if valid_obstacle_pos(x, pos, dir):
        #     valid_pos_count += 1
            # print(f"valid obstacle positions: {valid_pos_count}")
        if valid_obstacle_pos(x, tup, dir):
            valid_pos_count += 1
    return valid_pos_count

data2: np.ndarray[str, str] = data_parsed.copy()
print(f"result 2: {part2(data2)}")
