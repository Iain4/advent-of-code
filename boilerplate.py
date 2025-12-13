def boilerplate(day:int, path: str) -> str:
    """Returns some baisc boilerplate code for the advent of code problems"""

    return f"""
import sys
from aocd.post import submit
from typing import List

path =  sys.path[0]
sys.path.append("..")

with open("session.txt", "r") as s:
    session = s.read()
    s.close()
    
def parse_data(data:
    ...

def part_1(data):
    data = parse_data(data)


def part_2(data):
    data = parse_data(data)


if __name__ == "__main__":

    with open(path + f"/{day}.txt", "r") as f:
        data = f.readlines()
        f.close()

    print(part_1(data))
    # print(part_2(data))
    
    # submit(part_1(data), session=session, day={day})
"""
    
    