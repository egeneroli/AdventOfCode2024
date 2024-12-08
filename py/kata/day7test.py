from operator import add, mul
from numpy import base_repr
import re
puzzleInput=[list(map(int, re.findall('\d+', i))) for i in open(r'../../input/input7.txt', 'r')]
print(puzzleInput)
operatorLookup={'0':add, '1': mul, '2': lambda x,y:int(str(x)+str(y))}

def possibleOperators(length: int, base:int) -> iter:
    return (base_repr(i, base).rjust(length, '0') for i in range(base**length))

def returnFinal(operands: list, operators: str) -> int:
    result=operands[0]
    for number, operator in zip(operands[1:], operators, strict=True):
        result=operatorLookup[operator] (result, number)
    return result

def getAnswer(base: int) -> int:
    s=0
    for test, *operands in puzzleInput:
        for operator in possibleOperators(len(operands)-1, base):
            if returnFinal(operands, operator)==test:
                s+=test
                break
    return s

def part1():
    return getAnswer(2)
def part2():
    return getAnswer(3)

print(f"result 1: {part1()}\n")
# print(f"result 2: {part2()}\n")