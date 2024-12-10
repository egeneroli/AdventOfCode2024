import re
# import regex as re

from py.util import AOCKata


# part 1 solution
class Day9(AOCKata):
    def __init__(self, test: bool = False, print_input: bool = True) -> None:
        # call parent constructor to read in data
        super().__init__(9, test, print_input)
        self.diskmap: list[str] = self.build_initial_diskmap()

    # def guest_test(self) -> list[str]:
    #     free_space_locs, _, file = parse_disk(self.input_str)
    #     return rearrange_file(free_space_locs, list(file))

    def build_initial_diskmap(self):
        disk_map_lst: list[str] = []

        # iterate over all positions in input string
        for i, x in enumerate(self.input_str):
            id: int = int(i/2)
            n: int = int(x)

            s = str(id) if i%2 == 0 else "."
            s = s * n
            disk_map_lst.append(s)

        return disk_map_lst

    def get_all_file_blocks(self) -> list[int]:
        blocks: list[int] = []
        # get all file blocks
        for i in range(int((len(self.input_str) + 1) / 2)):
            index = i * 2
            blocks.extend([i for _ in range(int(self.input_str[index]))])
        return blocks

    def get_end_index(self) -> int:
        return sum(int(self.input_str[i]) for i in range(len(self.input_str)) if i % 2 == 0)

    def calculate_checksum(self, disk_map_lst: list[str]) -> int:
        return sum(i * int(x) for i, x in enumerate(disk_map_lst) if x.isdigit())

    def run(self) -> int:
        disk_map_lst: list[str] = []
        nums: list[int] = self.get_all_file_blocks()
        # print(f"nums: {nums}")

        # iterate over all positions in input string
        for i, x in enumerate(self.input_str):
            id: int = int(i/2)
            n: int = int(x)

            for _ in range(n):
                disk_map_lst.append(str(id if i%2 == 0 else nums.pop()))

        j = self.get_end_index()
        disk_map_lst = disk_map_lst[:j]
        disk_map_str = "".join(disk_map_lst)
        # print(disk_map_lst)
        # print(f"n_list: {len(disk_map_lst)}, n_str: {len(disk_map_str)}, j: {j}")
        # print(disk_map_str)

        # calculate "filesystem checksum" from final disk map by summing the product of each index and its value
        return self.calculate_checksum(disk_map_lst)

def part1() -> int:
    return Day9(test=False, print_input=False).run()

# print(f"result 1: {part1()}\n")


## part 2
class FileTooBig(Exception):
    pass

class Part2(Day9):

    def get_all_files(self) -> list[str]:
        files: list[str] = []
        # get all numbers that will be used
        for i in range(int((len(self.input_str) + 1) / 2)):
            index: int = i*2
            char: str = self.input_str[index]
            # files.extend([i for _ in range(int(char))])
            files.append(str(str(i) * int(char)))

        return files

    def get_file_indexes(self) -> list[int]:
        # return [i for i in range(len(self.diskmap)) if i%2 != 0]
        return [i for i, entry in enumerate(self.diskmap) if not entry.startswith(".") and entry]

    def get_space_indexes(self) -> list[int]:
        # return [i for i in range(len(self.diskmap)) if i%2 != 0]
        return [i for i, entry in enumerate(self.diskmap) if entry.startswith(".")]

    def get_file_index(self, file: str) -> int:
        return len(self.diskmap) - 1 - self.diskmap[::-1].index(file)

    def place_file(self, file: str):
        # file: str = self.diskmap[file_index]
        # print(f"file: {file}")
        # get spaces
        space_indexes: list[int] = self.get_space_indexes()

        for i in space_indexes:
            space: str = self.diskmap[i]
            space_size: int = len(space)
            file_size: int = len(file)
            # insert empty entries to maintain spaces as odd positions?
            # try to place file

            # handle single digit ID normally
            if file_size == 1 or self.has_single_digit_ID(file):
                if file_size <= space_size:
                    # place file in space
                    self.diskmap[i] = file
                    # replace file with dots
                    file_index: int = len(self.diskmap) - 1 - self.diskmap[::-1].index(file)
                    self.diskmap[file_index] = "."*len(file)
                    # insert remainder if exists
                    if space_size > file_size:
                        self.diskmap.insert(i+1, "."*(space_size - file_size))
                    break
            else:
                # handle > 1 digit ID case separately
                # break up and insert entry for each repeated ID
                # get ID
                pattern = r"(\d+?)\1+"
                re_match: re.Match = re.match(pattern, file)
                id: str = re_match.groups()[0]
                # print(f"re match group: {re_match.group()}, re match groups: {id}")

                # calculate number of repetitions
                file_size = len(re_match.group()) // len(id)

                # handle n like length -- this is the actual block length
                if file_size <= space_size:
                    # print("asdf")
                    # place / insert file / replace dots
                    for _ in range(file_size):
                        # place file in space
                        self.diskmap[i] = self.diskmap[i].replace(".", "", 1)
                        self.diskmap.insert(i, id)
                        i += 1

                    # replace file with dots
                    file_index: int = self.get_file_index(file)
                    # print(f"file_index: {file_index}")
                    self.diskmap[file_index] = "." * file_size

                    break

    def has_single_digit_ID(self, file: str) -> bool:
        return len(file) == file.count(file[0])

    def run(self) -> int:
        # get files for later
        files: list[str] = self.get_all_files()
        # print(f"files: {files}")
        # file_indexes: list[int] = self.get_file_indexes()
        # file_indexes = file_indexes[::-1]
        # print(f"file indexes: {file_indexes}")

        # check initial diskmap list is parse properly from constructor
        # print(self.diskmap)
        print("".join(self.diskmap))
        print(f"diskmap: {self.diskmap}")

        # iterate through files attempting to place at first free block
        index: int = 0
        for file in files[::-1]:
        # for i in range(len(file_indexes)):
            # place file if fits in a space, else discard file and do nothing
            self.place_file(file)
            # print(f"diskmap: {self.diskmap}")
            # print()

        print(self.diskmap)
        disk_map_str = "".join(self.diskmap)
        print(disk_map_str)
        # calculate "filesystem checksum" from final disk map by summing the product of each index and its value
        return self.calculate_checksum(self.diskmap)

def part2() -> int:
    return Part2(test=True, print_input=False).run()

print(f"result 2: {part2()}\n")


####### need to account for fact that files are coming through as whole blocks, not individual numbers
### need to separate for checksum calculation or it will be splitting digits on file IDs









