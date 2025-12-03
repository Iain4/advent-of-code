import sys
sys.path.append("..")
with open("session.txt", "r") as s:
    session = s.read()
    print(session)
    s.close()

from aocd.post import submit
from typing import List
path = "./advent-of-code-25/"



def find_joltage(bank: str) -> int:
    vals = [int(i) for i in bank]
    vals_ordered = sorted(vals)
    first_val = vals_ordered[-1]

    # quick redunancy check
    if first_val == vals_ordered[-2]:
        return int(str(first_val) * 2)
    
    index_1 = vals.index(first_val)
    
    if index_1 == len(vals) - 1:
        return int(str(vals_ordered[-2]) + str(first_val))

    # need to fix the case where the highest value is the last on in the list
    scnd_val = sorted(vals[index_1+1:])[-1]

    return int(str(first_val) + str(scnd_val))


def part_1(data: List[str]):
    jolt_tot = 0
    for bank in data:

        joltage = find_joltage(bank)
        jolt_tot += joltage
    
    return jolt_tot


if __name__ == "__main__":

    with open(path+"3.txt", "r") as f:
        data = f.read().splitlines()
        f.close()

    # print(part_1(data))
    submit(part_1(data), session=session)
