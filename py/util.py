"""
utility functions / classes
"""
# imports
from abc import ABC, abstractmethod


class AOCKata(ABC):
    """
    abstract base class for Advent of Code days/katas
    """

    def __init__(self, day: int, test: bool = False, print_input: bool = True) -> None:
        """
        kata class constructor -- read in input and stuff
        """
        # read in input
        self.day: int = day
        input_filename: str = f"input{self.day}"
        if test:
            input_filename += "test"
        self.input_str: str = read_input(input_filename, print_input)

    # define abstract method to be implemented by child classes
    @abstractmethod
    def run(self) -> int:
        raise NotImplementedError


def read_input(filename: str, print_input: bool = True) -> str:
    with open(f"input/{filename}.txt") as f:
        file: str = f.read()
        if print_input:
            print(f"input: \n{file}\n")
        return file.strip()

def str_replace(index: int, char: str, s: str) -> str:
    return s[:index] + char + s[index+1:]