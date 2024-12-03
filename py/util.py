def read_input(filename: str) -> list[str]:
    with open(f"input/{filename}.txt") as f:
        file: str = f.read()
        # print(f"input type: {type(file)}")
        return file.strip().split("\n")

def parse_matrix(x: list[str]) -> list[list[int]]:
    return [[int(x) for x in line.split()] for line in x]