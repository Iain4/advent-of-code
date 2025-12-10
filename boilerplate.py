def boilerplate(day:int, path: str) -> str:
    """Returns some baisc boilerplate code for the advent of code problems"""

    return f"""
import sys
from aocd.post import submit

path =  sys.path[0]
sys.path.append("..")

with open("session.txt", "r") as s:
    session = s.read()
    s.close()
    

def part_1(data):
    ...


def part_2(data):
    ...


if __name__ == "__main__":

    with open(path + f"/{day}.txt", "r") as f:
        data = f.read()
        f.close()

    print(part_1(data))
    # print(part_2(data))
    
    # submit(part_1(data), session=session, day={day})
"""
    
    