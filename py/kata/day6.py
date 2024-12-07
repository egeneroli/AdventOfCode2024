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
start_pos: tuple[int, int] = tuple([x[0] for x in np.where(np.isin(data_parsed, directions))])
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

def part1(x: np.ndarray[str, str], pos: tuple[int, int] = start_pos, dir: int = start_dir_index) -> int:
    # find starting position and direction
    while in_bounds(x, pos):
        pos, dir = walk(x, pos, dir)
    return np.sum(np.vectorize(is_visited)(x))

data: np.ndarray[str, str] = data_parsed.copy()
# part1(data)
print(f"result 1: {part1(data)}\n")
# print(data)

## part 2
RETRACE_THRESHOLD: int = 100
def is_loop(x: np.ndarray[str, str], pos: tuple[int, int], dir: int, retrace_threshold: int = RETRACE_THRESHOLD, visits: int = int(VISITED)) -> bool:
    retrace_count: int = 0
    visited: set[tuple[tuple[int, int], str]] = set()
    while in_bounds(x, pos):
        pos, dir = walk(x, pos, dir, visits)
        # print(f"pos: {pos}, dir: {dir}, retrace count: {retrace_count}")
        # print(x)
        try:  # increment retrace count if next position has been visited already
            next_pos: tuple[int, int] = step[dir](pos)
            next_char: str = x[next_pos]
            if (next_pos, directions[dir]) in visited:
                return True
            visited.add((next_pos, directions[dir]))
        except IndexError:
            pass
    return False
            # if is_obstacle(next_char):
            #     if next_pos in visited_obstacles.keys():
            #         if directions[dir] in visited_obstacles[next_pos]:
            #             print(visited_obstacles.__len__())
            #             for obs in visited_obstacles.keys():
            #                 print(f"obstacle pos: {tuple(int(ob) for ob in obs)}, directions: {visited_obstacles[obs]}")
            #             return True
            #         else:
            #             visited_obstacles[next_pos] += directions[dir]
            #     else:
            #         visited_obstacles[next_pos] = directions[dir]

                # print(f"obstacles: {obstacles}")
                # if visited_obstacles.count(next_pos) >= 2:
                #     return True
            # if is_visited(next_char):
            #     # determine if visited char needs to be updated
            #     visits = int(next_char) + 1
            #
            # #     if visits > 2:
            # #         retrace_count += 1
            # #
            # # # reset retrace count if next position is not visited and not an obstacle
            # elif not is_obstacle(next_char):
            #     retrace_count = 0
        # except IndexError:
        #     pass
        # break out if continuously retracing
        # if retrace_count >= retrace_threshold:
        #     return True
        # print(x)
    # if visited_obstacles.__len__() > 0:
    #     print(visited_obstacles.__len__())
    # for obs in visited_obstacles.keys():
    #     print(f"obstacle pos: {tuple(int(ob) for ob in obs)}, directions: {visited_obstacles[obs]}")
    # print()
    # return False

def valid_obstacle_pos(x: np.ndarray[str, str], pos: tuple[int, int], dir: int, retrace_threshold: int = RETRACE_THRESHOLD) -> bool:
    x_temp: np.ndarray[str, str] = x.copy()
    try:
        x_temp[step[dir](pos)] = OBSTACLE
    except IndexError:
        return False
    return is_loop(x_temp, pos, dir, retrace_threshold)

def part2(x: np.ndarray[str, str], pos: tuple[int, int] = start_pos, dir: int = start_dir_index, retrace_threshold: int = RETRACE_THRESHOLD) -> int:
    valid_pos_count: int = 0
    while in_bounds(x, pos):
        # while in bounds, patrol/walk like before
        pos, dir = walk(x, pos, dir)

        # after each step, check if putting obstacle in front of guard results in loop
        if valid_obstacle_pos(x, pos, dir, retrace_threshold):
            valid_pos_count += 1
            # print(f"valid obstacle positions: {valid_pos_count}")
    return valid_pos_count

# data2: np.ndarray[str, str] = data_parsed.copy()
# print(f"result 2: {part2(data2)}")
for n in [1, 10, 100, 1000, 10000, 100000, 1000000][:1]:
    data2: np.ndarray[str, str] = data_parsed.copy()
    print(f"result 2, n = {n}: {part2(data2, retrace_threshold=n)}")
    # print(data2)
