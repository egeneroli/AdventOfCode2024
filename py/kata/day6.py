from operator import index

from py.util import read_input
import numpy as np

# read in data
input_str: str = read_input("input6", False)

# parse data
data_parsed: np.ndarray[str, str] = np.array([list(row) for row in input_str.strip().split("\n")])

# define global variables
VISITED: str = "0"
VISITED_PATTERN: str = r"\d"
OBSTACLE: str = "#"
OBSTACLE_PATTERN: str = r"\#|X"
directions: list[str] = ["^", ">", "v", "<"]
start_pos: tuple[int, int] = tuple([int(x[0]) for x in np.where(np.isin(data_parsed, directions))])
start_dir_index: int = directions.index(data_parsed[start_pos])
# ^ -> row--, > -> col++, v -> row++, < -> col--
step: list = [lambda pos: (pos[0]-1, pos[1]), lambda pos: (pos[0], pos[1]+1), lambda pos: (pos[0]+1, pos[1]), lambda pos: (pos[0], pos[1]-1)]

## part 1
import re
def is_visited(char: str) -> bool:
    return bool(re.match(VISITED_PATTERN, str(char)))

def mark_visited(x: np.ndarray[str, str], pos: tuple[int, int], marker: str = VISITED) -> None:
    x[pos] = marker

def is_obstacle(char: str) -> bool:
    return bool(re.match(OBSTACLE_PATTERN, str(char)))

def increment_dir(dir_index: int) -> int:
    return (dir_index + 1) % 4

def walk(x: np.ndarray[str, str], pos: tuple[int, int], dir: int, visits: int = int(VISITED)) -> (int, int):
    # If there is something directly in front of you, turn right 90 degrees. Otherwise, take a step forward.
    new_pos: tuple[int, int] = step[dir](pos)
    # print(f"pos: {pos}, new_pos: {new_pos}, dir: {dir}")
    # print(x)

    try: # try to move forward (new_pos might be off the board)
        # mark position as visited
        mark_visited(x, pos, str(visits))
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

def patrol(x: np.ndarray[str, str], pos: tuple[int, int] = start_pos, dir: int = start_dir_index) -> int:
    visited: set[tuple[tuple[int, int], str]] = set()
    # find starting position and direction
    while in_bounds(x, pos):
        pos, dir = walk(x, pos, dir)
        # print(visited)
        if (pos, dir) in visited:
            # print(f"loop detected at {pos}, {dir}")
            # print(visited)
            raise Exception("loop detected")
        visited.add((pos, dir))
    return np.sum(np.vectorize(is_visited)(x))

def part1(x: np.ndarray[str, str]) -> int:
    return patrol(x)
data: np.ndarray[str, str] = data_parsed.copy()
# part1(data)
print(f"result 1: {part1(data)}\n")
# print(data)

## part 2
def is_loop(x: np.ndarray[str, str], pos: tuple[int, int], dir: int, visits: int = int(VISITED)) -> bool:
    visited: set[tuple[tuple[int, int], str]] = set()
    while in_bounds(x, pos):
        pos, dir = walk(x, pos, dir, visits)
        if (pos, dir) in visited:
            return True
        visited.add((pos, directions[dir]))
    return False

def valid_obstacle_pos(x: np.ndarray[str, str], pos: tuple[int, int], dir: int) -> bool:
    x_temp: np.ndarray[str, str] = x.copy()
    try:
        if x_temp[step[dir](pos)] == OBSTACLE or step[increment_dir(dir)](pos) == start_pos:
            return False
        x_temp[step[dir](pos)] = OBSTACLE
    except IndexError:
        return False
    return is_loop(x_temp, pos, dir)

def part2(x: np.ndarray[str, str], pos: tuple[int, int] = start_pos, dir: int = start_dir_index) -> int:
    valid_pos_count: int = 0
    # while in_bounds(x, pos):
    #     # while in bounds, patrol/walk like before
    #     pos, dir = walk(x, pos, dir)
    #
    #     try:
    #         x_temp: np.ndarray[str, str] = x.copy()
    #         x_temp[step[dir](pos)] = OBSTACLE
    #         patrol(x_temp, pos, dir)
    #     except Exception:
    #         valid_pos_count += 1
    #         print(f"valid obstacle positions: {valid_pos_count}")
    x_temp: np.ndarray[str, str] = x.copy()
    x_temp[(6,3)] = OBSTACLE
    try:
        result = patrol(x_temp, pos, dir)
    except Exception:
        print("loop detected")
        return valid_pos_count

        # after each step, check if putting obstacle in front of guard results in loop
        # if valid_obstacle_pos(x, pos, dir):
        #     valid_pos_count += 1
        #     print(f"valid obstacle positions: {valid_pos_count}")
    return valid_pos_count

data2: np.ndarray[str, str] = data_parsed.copy()
print(f"result 2: {part2(data2)}")
