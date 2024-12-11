import re

from py.util import AOCKata

# define string constants
SPACE: str = "."
INDEX: str = "index"
ID: str = "id"
N_BLOCKS: str = "n_blocks"
SLUG: str = "slug"

# part 1 solution
class Day9(AOCKata):

    def __init__(self, test: bool = False, print_input: bool = True) -> None:
        # call parent constructor to read in data
        super().__init__(9, test, print_input)
        self.diskmap: list[str] = self.build_initial_diskmap()
        self.diskmap_dicts: list[dict] = self.build_initial_diskmap_dicts()

    def build_initial_diskmap(self):
        disk_map_lst: list[str] = []

        # iterate over all positions in input string
        for i, x in enumerate(self.input_str):
            id: int = int(i/2)
            n: int = int(x)

            s = str(id) if i%2 == 0 else SPACE
            s = s * n
            disk_map_lst.append(s)

        return disk_map_lst

    def build_initial_diskmap_dicts(self) -> list[dict[str, str|int]]:
        disk_map: list[dict] = []

        # iterate over all positions in input string
        disk_map_index: int = 0
        for i, x in enumerate(self.input_str):
            id: int = int(i/2)
            n: int = int(x)

            s: str = str(id) if i%2 == 0 else SPACE
            map: dict[str, str|int] = {ID: s, N_BLOCKS: n, SLUG: s * n, INDEX: disk_map_index}
            disk_map.append(map)
            disk_map_index += 1

        return disk_map

    def get_all_files(self) -> list[str]:
        files: list[str] = []
        # get all numbers that will be used
        for i in range(int((len(self.input_str) + 1) / 2)):
            index: int = i*2
            char: str = self.input_str[index]
            # files.extend([i for _ in range(int(char))])
            files.append(str(str(i) * int(char)))

        return files

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

    def get_all_files(self) -> list[dict]:
        return self.get_all(self.is_file)

    def get_all_spaces(self) -> list[dict]:
        return self.get_all(self.is_space)

    def get_all(self, condition: callable) -> list[dict]:
        lst: list[dict] = []
        # print(self.diskmap_dicts)
        # for i, map in self.diskmap_dicts:
        for i in range(len(self.diskmap_dicts)):
            map: dict[str, str|int] = self.diskmap_dicts[i]
            if condition(map):
                lst.append(map)
        return lst

    def is_space(self, entry: dict) -> bool:
        return entry[ID] == SPACE

    def is_file(self, entry: dict) -> bool:
        return entry[ID] != SPACE

    def get_updated_file(self, file: dict[str, str|int]) -> dict[str, str|int]:
        file: dict = next(iter([e for e in self.diskmap_dicts if e[ID] == file[ID]][::-1]), None)
        if not file:
            return None
        file[INDEX] = len(self.diskmap_dicts) - 1 - file[INDEX]
        return file

    def get_next_space(self, file: dict[str, str|int]) -> dict[str, str|int]:
        if file is None:
            return None
        return next((s for _, s in enumerate(self.diskmap_dicts) if self.is_space(s) and s[N_BLOCKS] >= file[N_BLOCKS]), None)

    def update_space_index(self, space: dict[str, str|int]) -> None:
        space[INDEX] = next((i for i, s in enumerate(self.diskmap_dicts) if self.is_space(s) and s[N_BLOCKS] >= space[N_BLOCKS]), None)

    def update_file_index(self, file: dict[str, str|int]) -> dict[str, str|int]:
        file: dict = next(iter([e for e in self.diskmap_dicts if e[ID] == file[ID]][::-1]), None)
        if not file:
            return None
        file[INDEX] = len(self.diskmap_dicts) - 1 - file[INDEX]

    def get_group_list(self) -> list[str]:
        return [dct[SLUG] for dct in self.diskmap_dicts]

    def get_block_list(self) -> list[str]:
        lst: list[str] = []
        for dct in self.diskmap_dicts:
            for _ in range(dct[N_BLOCKS]):
                lst.append(dct[ID])
        return lst

    def get_diskmap_str(self) -> str:
        return "".join(self.get_block_list())

    def update_indexes(self, min: int = 0) -> None:
        for i in range(min, len(self.diskmap_dicts)):
            self.diskmap_dicts[i][INDEX] = i

    def place_file(self, file: dict[str, str|int]) -> None:
        # print(f"** place_file **")
        # get first space that is big enough to hold file or none if no space is big enough
        space: dict[str, str|int] = self.get_next_space(file)
        print(f"\nfile: {file}, space: {space}")
        self.print_diskmap()

        # if no space is big enough, raise error
        if not space:
            raise FileTooBig(f"file: {file} is too big to fit in any space")
        # print(f"file: {file}, space: {space}")

        # space bigger than file, need to deal with remainder
        if file[N_BLOCKS] < space[N_BLOCKS]:
            self.update_indexes()
            # print("** remainder")
            # self.print_diskmap()
            # calculate remainder, update original space before swapping
            # print(f"file: {file}, space: {space}")
            space, remainder = self.get_remainder(file, space)
            print(f"file: {file}, space: {space}, remainder: {remainder}")

            # insert remainder immediately after space
            self.print_diskmap()
            self.diskmap_dicts.insert(space[INDEX]+1, remainder)
            # test adding zero length space
            # self.diskmap_dicts.insert(space[INDEX]+1, {ID: ".", N_BLOCKS: 0, SLUG: "", INDEX: space[INDEX]+1})
            self.print_diskmap()
            # update file index from inserting a space
            # print(f"file: {file}")
            # if space[INDEX] < file[INDEX]:
            #     print("index updated")
            #     print(f"file: {file}")
            #     file[INDEX] += 1
            self.update_indexes(space[INDEX]+1)


        # swap space and file
        print("********** before swap")
        self.print_diskmap()
        # self.update_space_index(space)
        # self.update_space_index(file)
        self.update_indexes()
        self.swap_elements(space, file)
        self.print_diskmap()
        print("********** after swap")

    def get_remainder(self, file: dict, space: dict) -> (dict[str, str|int], dict[str, str|int]):
        # calculate difference in size
        diff: int = space[N_BLOCKS] - file[N_BLOCKS]
        remainder: dict[str, str|int] = {ID: space[ID],
                                         N_BLOCKS: diff,
                                         SLUG: space[ID]*diff,
                                         INDEX: space[INDEX]+1}
        # update original space properties
        space[N_BLOCKS] = file[N_BLOCKS]  # n blocks is now same as file
        space[SLUG] = SPACE * space[N_BLOCKS] # update slug for new length
        return space, remainder

    def swap_elements(self, e1: dict, e2: dict) -> None:
        e2_index: int = e2[INDEX]
        # overwrite element 1 with element 2
        e2[INDEX] = e1[INDEX]
        self.diskmap_dicts[e1[INDEX]] = e2

        # overwrite element 2 with elment 1
        e1[INDEX] = e2_index
        self.diskmap_dicts[e2_index] = e1

    def run(self) -> int:
        print(f"** run **")
        # get files for later
        files: list[dict] = self.get_all_files()
        # print(f"files: {files}")

        # check initial diskmap list is parse properly from constructor
        self.print_diskmap()
        # print("".join(self.diskmap))
        # print(f"diskmap: {self.diskmap}")

        # iterate through files attempting to place at first free block
        for file in files[::-1]:
            # print(f"\nfile: {file}")
            # self.print_diskmap()
            # file: dict[str, str|int] = self.get_updated_file(file)
            self.print_diskmap()
            # place file if fits in a space, else discard file and do nothing
            try:
                self.place_file(file)
            except FileTooBig:
                pass
            # self.print_diskmap()
            # print()
        self.print_diskmap()

        # break up blocks to calculate checksum
        # print(f"is repeating: {is_repeating}")
        lst = self.split_repeated(self.diskmap)
        # print(f"diskmap: {lst}")

        # calculate "filesystem checksum" from final disk map by summing the product of each index and its value
        return self.calculate_checksum(lst)

    def print_diskmap(self):
        # print(self.diskmap_dicts)
        print(self.get_group_list())
        # print(self.get_diskmap_str())

    def split_repeated(self, diskmap: list[str]) -> list[str]:
        lst: list[str] = []
        for s in diskmap:
            if self.is_repeating(s) or self.is_repeating(s, r"\.\.+"):
                lst.extend(list(s))
            else:
                lst.append(s)
        return lst

    def is_repeating(self, s: str, pattern: str = r"(\d+?)\1") -> bool:
        return bool(re.match(pattern, s))

def part2() -> int:
    return Part2(test=True, print_input=False).run()

print(f"result 2: {part2()}\n")









