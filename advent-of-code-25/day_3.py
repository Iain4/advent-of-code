import sys
sys.path.append("..")
with open("session.txt", "r") as s:
    session = s.read()
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


def find_overdrive_joltage(bank:str, max_batteries: int, batteries_used: int = 0, current_joltage: str = '', search_order: int = 1):
    # this recursivly finds the 12 digits going left to right in the bank that together makes the largest value

    batteries_left = max_batteries - batteries_used
    if batteries_left == 0:
        return current_joltage
    
    elif len(bank) == batteries_left:
        return current_joltage + bank
    
    elif search_order > batteries_left:
        raise ValueError("search_order bang out of order")

    vals = [int(i) for i in bank]
    first = sorted(vals)[-search_order]
    f_index = vals.index(first)

    # recursively looking down the sorted list until there is enough batteries left
    if len(vals[f_index:]) < batteries_left:
        current_joltage = find_overdrive_joltage(bank, max_batteries, batteries_used, current_joltage, search_order+1)
    
    else:
        current_joltage = find_overdrive_joltage(bank[f_index+1:], max_batteries, batteries_used+1, current_joltage+str(first), 1)

    return current_joltage


def part_2(data: List[str]) -> int: 
    joltage = 0
    for bank in data:
        joltage += int(find_overdrive_joltage(bank, 12))

    return joltage        

if __name__ == "__main__":

    with open(path+"3.txt", "r") as f:
        data = f.read().splitlines()
        f.close()

    # print(part_1(data))
    # print(part_2(data))

    submit(part_2(data), session=session)