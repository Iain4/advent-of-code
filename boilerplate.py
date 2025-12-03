def boilerplate(day:int, path: str) -> str:
    """Returns some baisc boilerplate code for the advent of code problems"""

    return f"""
from aocd.post import submit

def part_1(data):
    ...


def part_2(data):
    ...


if __name__ == "main":

    with open(f{day}.txt", "r") as f:
        data = f.read()
        f.close()


    # submit(part_1(data))
"""
    
    