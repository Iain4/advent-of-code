
from aocd.post import submit
from getData import path

from typing import List


def find_joltage(bank: str):
    
    vals = [int(i) for i in bank]
    vals_ordered = sorted(vals)
    first_val = vals_ordered[-1]

    # quick redunancy check
    if first_val == vals_ordered[-2]:
        return str(first_val) * 2
    
    index_1 = vals.index(first_val)

    # need to fix the case where the highest value is the last on in the list
    scnd_val = sorted(vals[index_1+1:])[-1]

    return int(str(first_val) + str(scnd_val))


def part_1(data: List[str]):
    jolt_tot = 0
    for bank in data:

        joltage = find_joltage(bank)
        jolt_tot += joltage
    
    return jolt_tot


if __name__ == "main":

    with open(path + "3.txt", "r") as f:
        data = f.read().splitlines()
        f.close()

    print(part_1(data))
    
    # submit(part_1(data))
