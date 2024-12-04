from py.util import read_input, parse_str_matrix

# read in data
input_str: str = read_input("input4")

# parse into list of strings
data: list[str] = input_str.split("\n")

WORD: str = "XMAS"

# part 1 solution
def search(s: str, word: str = WORD) -> int:
    return s.count(word) + s[::-1].count(word)

def search_rows(x: list[str]) -> int:
    return sum(search(row) for row in x)

def search_cols(x: list[str]) -> int:
    return sum(search("".join([row[i] for row in x])) for i in range(0, len(x[0])))

def search_diags(x: list[str], word: str = WORD) -> int:
    # search principal diagonals starting on left edge, then top edge
    return sum(search("".join([x[i+j][j] for j in range(len(x)-i)]), word) for i in range(0, len(x))) \
        + sum(search("".join([x[j][i+j] for j in range(len(x[i])-i)]), word) for i in range(1, len(x[0])))

def part1() -> int:
    """
    search each row, column, and diagonal for the word (forward and backward)
    :return: total word count
    """
    # declare counter
    count: int = 0

    # search rows
    count += search_rows(data)

    # search columns
    count += search_cols(data)

    # search principal diagonals
    count += search_diags(data)

    # search secondary diagonals by flipping matrix horizontally
    count += search_diags([row[::-1] for row in data])

    return count

print(f"result 1: {part1()}\n")

## part 2
# part 2 solution
def part2() -> int:
    """
    check each 3x3 window for X-MAS pattern
    :return: total count of X-MAS patterns
    """
    WORD: str = "MAS"

    # declare counter
    count: int = 0

    # loop over each 3x3 window by getting starting positions
    for i in range(0, len(data) - 2):
        for j in range(0, len(data[0]) - 2):
            # get window
            mat: list[str] = [data[i+k][j:j+3] for k in range(3)]

            # check for X by searching principal and secondary diagonals
            if 1 == search_diags(mat, WORD) == search_diags([row[::-1] for row in mat], WORD):
                count += 1

    return count

print(f"result 2: {part2()}")













