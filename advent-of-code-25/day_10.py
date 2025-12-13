
import sys
from aocd.post import submit
from typing import List

path =  sys.path[0]
sys.path.append("..")

with open("session.txt", "r") as s:
    session = s.read()
    s.close()
    
def parse_data(data, with_joltage = False):
    # The lights and buttons are binary representations of being on/off / which light they change.
    # They are decimal integers though because that what python does.
    # Both the lights and buttons are done the same so I can just xor them later.
    data = data.copy()
    for i, line in enumerate(data):
        line = line.split()
        joltages = line.pop()
        
        # changing the light into binary
        lights = 0
        for n, char in enumerate(line[0].strip("[]")):
            if char == '#':
                lights += 2 ** n

        # changing the buttons into binary
        buttons = []
        for string in line[1:]:
            button = 0
            for char in string:
                if char.isdecimal(): button += 2 ** int(char)
            buttons += [button]

        if with_joltage:
            data[i] = [lights, buttons, joltages]
        else:
            data[i] = [lights, buttons]
    return data


def int_xor_list(but1: int, buttons: List[int], goal: int):
    res = []
    for b in buttons:
        val = but1 ^ b
        res += [val]
        if val == goal:
            return res, True
    return res, False


def search_next_depth(buttons: List[list], goal: int):
    new_bs = []
    done = False

    # even depth search
    if len(buttons) == 1:
        buttons = buttons[0]
        for i, b1 in enumerate(buttons):
            res, done = int_xor_list(b1, buttons[i+1:], goal)
            new_bs += res
            if done:
                return new_bs, True
        return new_bs, False
    
    # odd depth
    b1s, b2s = buttons[0], buttons[1]
    for b1 in b1s:
        res, done = int_xor_list(b1, b2s, goal)
        new_bs += res
        if done: 
            return new_bs, True
    return new_bs, False


def recursive_search(buttons:List[list], goal: int, depth: int = 0):
    i = int(depth/2)
    if depth % 2 == 0:
        new_buttons, done = search_next_depth([buttons[i]], goal)
    else:
        new_buttons, done = search_next_depth(buttons[i:i+2], goal)
    buttons += [new_buttons]
    if done:
        return depth
    depth = recursive_search(buttons, goal, depth + 1)
    return depth


def catch_edge_cases(buttons: List[int], light:int):
    if light == 0:
        return 0, True
    elif light in buttons:
        return 1, True
    return 0, False


def part_1(data):
    data = parse_data(data)
    button_presses = 0

    for line in data:
        light, buttons = line

        res, done = catch_edge_cases(buttons, light)
        if done:
            button_presses += res
            continue

        depth = recursive_search([buttons], light)

        # 0 and 1 press cases cause and so depth 0 corresponds to 2 button presses 
        button_presses += (depth + 2)

    return button_presses


def part_2(data):
    ...


if __name__ == "__main__":

    with open(path + f"/10.txt", "r") as f:
        data = f.readlines()
        f.close()

    print(part_1(data))
    # print(part_2(data))
    
    submit(part_1(data), session=session, day=10)
