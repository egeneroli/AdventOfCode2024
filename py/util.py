def read_input(filename: str) -> list[str]:
    with open(f"input/{filename}.txt") as f:
        file: str = f.read()
        # print(f"input type: {type(file)}")
        return file.strip().split("\n")

