
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


def find_accessible_paper(data):
    accessible_paper = []
    for r, text in enumerate(data):
        for c in range(len(text)):
            if text[c] == '.':
                continue
            elif can_forklift_access(data, r, c):
                accessible_paper += [(r,c)]

    return accessible_paper


def remove_accessed_paper(data: List[str], accessible_paper: List[tuple]) -> List[str]:
    for (r, c) in accessible_paper:
        text = data[r]
        data[r]  = f"{text[:c]}.{text[c+1:]}"
    return data


def part_2(data):
    num_removed = 0

    while True:
        accessible = find_accessible_paper(data)

        if len(accessible) == 0:
            # with open("4_after.txt", "w") as f:
            #     for line in data:
            #         f.write(line + "\n")
            #     f.close()                    
            return num_removed
        
        num_removed += len(accessible)
        data = remove_accessed_paper(data, accessible)


if __name__ == "__main__":

    with open(path + f"/4.txt", "r") as f:
        data = f.read().splitlines()
        f.close()

    # print(len(find_accessible_paper(data)))
    print(part_2(data))

    # submit(part_2(data), session=session)
