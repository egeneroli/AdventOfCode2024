def read_input(filename: str, print_input: bool = True) -> str:
    with open(f"input/{filename}.txt") as f:
        file: str = f.read()
        if print_input:
            print(f"input: {file}\n")
        return file.strip()

def parse_matrix(x: list[str]) -> list[list[int]]:
    return [[int(x) for x in line.split()] for line in x]