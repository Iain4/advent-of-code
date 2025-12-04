
import sys
from aocd.post import submit
from typing import List

path = sys.path[0]
sys.path.append("..")

with open("session.txt", "r") as s:
    session = s.read()
    s.close()


def can_forklift_access(data: List[str], row: int, col: int, too_many_adj: int = 4) -> bool:
    adjacent_paper = 0
    test_points = get_adjacent_points(data, row, col,)
    
    for p in test_points:
        if data[p[0]][p[1]] in '@':
            adjacent_paper += 1

    if adjacent_paper < too_many_adj:
        return True
    
    return False


def get_adjacent_points(data: List[str], row: int, col: int) -> List[tuple]:
    rows = get_coord_points(row, len(data) - 1)
    cols = get_coord_points(col, len(data[col]) - 1)
    points = [(r,c) for r in rows for c in cols if not (r == row and c == col)]
    return points


def get_coord_points(coord: int, coord_max: int, coord_min: int = 0) -> List:
    if coord == coord_min:
        return [coord, coord + 1]
    elif coord == coord_max:
        return [coord - 1, coord]
    return [coord-1, coord, coord+1]


def part_1(data):
    accessible_paper = 0
    for r, text in enumerate(data):
        for c in range(len(text)):
            if text[c] == '.':
                continue
            elif can_forklift_access(data, r, c):
                accessible_paper += 1

    return accessible_paper


def part_2(data):
    ...


if __name__ == "__main__":

    with open(path + f"/4.txt", "r") as f:
        data = f.read().splitlines()
        f.close()

    # print(part_1(data))
    # print(part_2(data))

    # submit(part_1(data), session=session)
