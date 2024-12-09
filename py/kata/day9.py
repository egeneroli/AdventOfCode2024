import re

from py.kata.day9test import rearrange_file, parse_disk
from py.util import AOCKata, str_replace


# part 1 solution
class Day9(AOCKata):
    def __init__(self, test: bool = False, print_input: bool = True) -> None:
        # call parent constructor to read in data
        super().__init__(9, test, print_input)
        # parse data
        disk_map_dicts, disk_map_str = self.build_disk_map()
        self.disk_map_dicts: list[dict[str, str|int]] = disk_map_dicts
        self.disk_map_str: str = disk_map_str
        # self.disk_map_list: list[str] = list(disk_map_str)

    def build_disk_map(self) -> (list[tuple[str, int]], str):
        # parse data / build "disk map" string
            # alternate char between ID (basic counter, start at 0) and '.' (free space)
            # repeat char as many times as element in data
        disk_map_str: str = ""
        disk_map: list[dict[str, str|int]] = []
        for i, x in enumerate(self.input_str):
            char: str = str(int(i/2)) if i%2 == 0 else "."
            repeats: int = int(x)
            disk_map.append({"char": char, "n": repeats})
            disk_map_str += char * repeats

        return disk_map, disk_map_str

    def guest_test(self) -> list[str]:
        free_space_locs, _, file = parse_disk(self.input_str)
        return rearrange_file(free_space_locs, list(file))

    def run(self) -> int:
        nums: list[int]  = [map["char"] for map in self.disk_map_dicts for _ in range(map["n"]) if map["char"] != "."]
        disk_map_list: list[str] = list(self.disk_map_str[:len(nums)])
        n_dots: int = self.disk_map_str[:len(nums)].count(".")
        # print(f"input: {self.input_str}")
        # print(self.disk_map_str)
        # print(f"len nums: {len(nums)}, nums: {nums}")
        # print(f"dots to replace: {n_dots}")
        # print(f"nums: {nums}")
        block_index: int = 0
        # iterate over all dots to replace
        for _ in range(n_dots):
            # get index of next empty space
            while disk_map_list[block_index] != ".":
                block_index += 1
            # replace empty space with num
            if disk_map_list[block_index] == ".":
                num = nums.pop()
                disk_map_list[block_index] = num
                # print(f"{''.join(disk_map_list)}, i: {block_index}, num: {num}")
        # disk_map_list = disk_map_list[:len(nums)]  # + ["." * len(disk_map_list[:len(nums)])]
        print(disk_map_list)
        disk_map_list_test = self.guest_test()
        indexes: list[int] = [i for i in range(len(disk_map_list)) if disk_map_list[i] != disk_map_list_test[i]]
        print(indexes[:100])
        # disk_map_str: str = "".join(disk_map_list)
        # print(disk_map_str)

        # calculate "filesystem checksum" from final disk map by summing the product of each index and its value
        return sum(i * int(x) for i, x in enumerate(disk_map_list))

def part1() -> int:
    return Day9(test=False, print_input=False).run()

print(f"result 1: {part1()}\n")


## part 2
class Part2(Day9):

    def run(self) -> int:
        return -1

def part2() -> int:
    return Part2().run()

# print(f"result 2: {part2()}\n")













