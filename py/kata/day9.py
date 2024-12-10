from py.util import AOCKata


# part 1 solution
class Day9(AOCKata):
    def __init__(self, test: bool = False, print_input: bool = True) -> None:
        # call parent constructor to read in data
        super().__init__(9, test, print_input)

    # def guest_test(self) -> list[str]:
    #     free_space_locs, _, file = parse_disk(self.input_str)
    #     return rearrange_file(free_space_locs, list(file))

    def get_all_file_blocks(self) -> list[int]:
        nums: list[int] = []
        # get all numbers that will be used
        for i in range(int((len(self.input_str) + 1) / 2)):
            index = i * 2
            nums.extend([i for _ in range(int(self.input_str[index]))])
        return nums

    def get_end_index(self) -> int:
        return sum(int(self.input_str[i]) for i in range(len(self.input_str)) if i % 2 == 0)

    def calculate_checksum(self, disk_map_lst: list[str]) -> int:
        return sum(i * int(x) for i, x in enumerate(disk_map_lst))

    def run(self) -> int:
        disk_map_lst: list[str] = []
        nums: list[int] = self.get_all_file_blocks()
        # print(f"nums: {nums}")

        # iterate over all positions in input string
        for i, x in enumerate(self.input_str):
            id: int = int(i/2)
            n: int = int(x)

            for _ in range(n):
                # add id n times to result if file (i is even)
                # if i%2 == 0:
                #     disk_map_lst.append(str(id))
                # add next number from end of file blocks list n times to result
                # else:
                #     disk_map_lst.append(str(nums.pop()))
                disk_map_lst.append(str(str(id) if i%2 == 0 else nums.pop()))

            # disk_map_lst.append(s)
            # print("".join(disk_map_lst))

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

print(f"result 1: {part1()}\n")


## part 2
class Part2(Day9):

    def run(self) -> int:
        return -1

def part2() -> int:
    return Part2().run()

# print(f"result 2: {part2()}\n")













