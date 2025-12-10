
import sys
from aocd.post import submit
from typing import List

path =  sys.path[0]
sys.path.append("..")

with open("session.txt", "r") as s:
    session = s.read()
    s.close()
    

def beam_step(beams: dict, next_layer: str, quantum=False):
    split_count = 0
    next_beams = {}

    for beam in beams:
        if next_layer[beam] == '^':
            if quantum:
                split_count += 1 * beams[beam]
            else:
                split_count += 1
            new_beam = [beam-1, beam+1]
        else:
            new_beam = [beam]
        for b in new_beam:
            if b in next_beams:
                next_beams[b] += beams[beam]
            else:
                next_beams[b] = beams[beam]

    return next_beams, split_count


def main(data, part_2=False):
    beams = {data[0].index('S'): 1}
    split_total = 1
    for line in data[1:]:
        beams, splits = beam_step(beams, line, part_2)
        split_total += splits
    return split_total


if __name__ == "__main__":

    with open(path + f"/7.txt", "r") as f:
        data = f.readlines()
        f.close()

    # print(main(data))
    print(main(data, part_2 = True))
    
    submit(main(data, part_2=True), session=session, day=7)
