
import sys
from aocd.post import submit

path =  sys.path[0]
sys.path.append("..")

with open("session.txt", "r") as s:
    session = s.read()
    s.close()


def part_1(ranges, ids):
    fresh_ids = 0
    for id in ids:
        for r in ranges:
            if id >= r[0] and id <= r[1]:
                fresh_ids += 1
                break
    return fresh_ids

    
def check_range(agg_r, new_r) -> list | None:
    # if agg_r == new_r:
    #     raise RecursionError("This item should've been removed from the list")

    best_r = agg_r.copy()
    # checking if they are completely seperate
    if new_r[0] > agg_r[1] or new_r[1] < agg_r[0]:
        return None
    
    if new_r[0] < agg_r[0]:
        best_r[0] = new_r[0]
    if new_r[1] > agg_r[1]:
        best_r[1] = new_r[1]
    return best_r


def aggregate_range(agg_rs, new_r, i=0):
    for a in agg_rs:
        if new_r is None:
            break
        val = check_range(a, new_r)

        if val is not None:
            new_r = val
            agg_rs.remove(a)
            agg_rs, new_r = aggregate_range(agg_rs, new_r, i=i+1)

    if new_r is None:
        return agg_rs, None
    return agg_rs + [new_r], None


def part_2(ranges):
    agg_rngs = [ranges[0]]
    for r in ranges[1:]:
        agg_rngs, _ = aggregate_range(agg_rngs, r)

    num_fresh = 0
    for l in agg_rngs:
        num_fresh += l[1] - l[0] + 1
    return num_fresh




def parse_input(input: str):
    split = input.index("\n\n")
    fresh_ranges = input[:split].splitlines()
    fresh_ranges = [list(map(int, s.split("-"))) for s in fresh_ranges]
    ingredient_ids = input[split+2:].splitlines()
    ingredient_ids = [int(i) for i in ingredient_ids]
    return fresh_ranges, ingredient_ids


if __name__ == "__main__":

    with open(path + f"/5.txt", "r") as f:
        ranges, ids = parse_input(f.read())
        f.close()

    print(part_2(ranges))
    
    submit(part_2(ranges), session=session, day=5)
