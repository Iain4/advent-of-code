
import sys
from aocd.post import submit
from typing import List

import cProfile
import pstats

 # TODO: Clean up the unsuccessful part 2 bits from this


path =  sys.path[0]
sys.path.append("..")

with open("session.txt", "r") as s:
    session = s.read()
    s.close()
    

def parse_data(data, for_part_2 = False):
    # The lights and buttons are binary representations of being on/off / which light they change
    # They are decimal integers though because that what python does
    # Both the lights and buttons are done the same so I can just xor them later
    data = data.copy()

    for i, line in enumerate(data):
        line = line.split()

        joltage = line.pop()

        if for_part_2:
            joltage = jolt_list_to_int([int(j) for j in joltage.strip("{}").split(",")])

            # this button bit is horrendous but it works
            buttons = set()
            for bs in line[1:]:
                bs = list(map(int, bs.strip("()").split(",")))
                new_button = [ 
                    1 if x in bs else 0
                    for x in range(bs[-1] + 1)
                ]
                buttons.add(jolt_list_to_int(new_button))

            data[i] = [joltage, buttons]

        else:
            # changing the light into binary
            lights = 0
            for n, char in enumerate(line[0].strip("[]")):
                if char == '#':
                    lights += 2 ** n

            # changing the buttons into binary for part 1
            buttons = []
            for string in line[1:]:
                button = 0
                for char in string:
                    if char.isdecimal(): button += 2 ** int(char)
                buttons += [button]

            data[i] = [lights, buttons]
    return data



def search_next_depth(buttons: list, goal, search_func):
    new_bs = set()
    done = False
    
    if len(buttons) == 1:
        b1s, b2s = buttons[0], buttons[0]
    else:
        b1s, b2s = buttons[0], buttons[1]

    for b1 in b1s:
        res, done = search_func(b1, b2s, goal)
        new_bs = new_bs.union(res)
        if done: 
            return new_bs, True
    return new_bs, False


def recursive_search(buttons: list, goal, search_func, depth: int = 0, ):
    # i should properly define what the search func is / can be
    # but i'm just making this work for part 2 so hey ho
    i = int(depth/2)
    if depth % 2 == 0:
        new_buttons, done = search_next_depth([buttons[i]], goal, search_func)
    else:
        new_buttons, done = search_next_depth(buttons[i:i+2], goal, search_func)
    buttons += [new_buttons]

    # print(depth)

    if done:
        return depth
    depth = recursive_search(buttons, goal, search_func, depth + 1)
    return depth


def find_result(data, search_func):
    button_presses = 0

    for line in data:
        goal, buttons = line

        res, done = catch_edge_cases(buttons, goal)
        if done:
            button_presses += res
            continue

        depth = recursive_search([buttons], goal, search_func)
        # 0 and 1 press cases cause and so depth 0 corresponds to 2 button presses 
        button_presses += (depth + 2)
        # break
    return button_presses


def catch_edge_cases(buttons: int, goal: int | List[int]):
    # need to check if all the joltages are 0
    if goal == 0:
        return 0, True
    elif goal in buttons:
        return 1, True
    return 0, False


def int_xor_list(but1: int, buttons: List[int], goal: int):
    res = set()
    for b in buttons:
        val = but1 ^ b
        res.add(val)
        if val == goal:
            return res, True
    return res, False


def part_1(data):
    data = parse_data(data)
    presses = find_result(data, int_xor_list)
    return presses


def jolt_list_to_int(values: List[int]) -> int:
    res = 0
    for i, val in enumerate(values):
        res += val * 1000 ** i
    return res


def joltage_adder(but1, buttons, goal):
    new_buttons = set()
    for b in buttons:
        val = but1 + b
        new_buttons.add(val)
        if val == goal:
            return new_buttons, True
    return new_buttons, False


def part_2(data):
    data = parse_data(data, True)
    presses = find_result(data, joltage_adder)
    return presses


if __name__ == "__main__":

    with open(path + f"/10test.txt", "r") as f:
        data = f.readlines()
        f.close()

    # print(part_1(data))
    with cProfile.Profile() as pr:
        print(part_2(data))
    
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats(10)
    
    # submit(part_1(data), session=session, day=10)
