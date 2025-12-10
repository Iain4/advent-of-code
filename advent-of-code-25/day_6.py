
import sys
from aocd.post import submit
from typing import List


path =  sys.path[0]
sys.path.append("..")

with open("session.txt", "r") as s:
    session = s.read()
    s.close()
    

def parse_data_p1(data: List[str]):
    d = data.copy()
    operands = d.pop().split()
    vals = [list(map(int, v.split())) for v in d]
    return vals, operands


def operate(vals, operator):
    if operator == '+':
        return sum(vals)
    elif operator =='*':
        tot = 1
        for v in vals:
            tot *= v
        return tot


def part_1(data):
    vals, operands = parse_data_p1(data)
    total = 0
    for n, o in enumerate(operands):
        total += operate([v[n] for v in vals], o)
    return total



def parse_data_p2(data):
    d = data.copy()
    operands = d.pop()
    return d, operands


def get_next_interval(start: int, operands: str) -> tuple:
    for n, o in enumerate(operands[start+1:]):
        if o != ' ':
            return start, start + n
    return start, len(operands)

def get_numbers(vals, start, stop) -> List[int]:
    numbers = []
    for i in range(start, stop):
        num = ''
        for v in vals:
            if v[i] != ' ':
                num += v[i]
        if num:
            numbers += [int(num)]
    return numbers


def part_2(data):
    vals, operands = parse_data_p2(data)
    total = 0
    i = 0
    while i <= len(operands):
        start, stop = get_next_interval(i, operands)
        numbers = get_numbers(vals, start, stop)
        total += operate(numbers, operands[start])
        i = stop + 1
    return total

if __name__ == "__main__":

    with open(path + f"/6.txt", "r") as f:
        data = f.readlines()
        f.close()

    print(part_1(data))
    print(part_2(data))
    
    # submit(part_2(data), session=session, day=6)
