
import sys
from aocd.post import submit
from typing import List
import numpy as np
import matplotlib.pyplot as plt

path =  sys.path[0]
sys.path.append("..")

with open("session.txt", "r") as s:
    session = s.read()
    s.close()


def get_area(p1, p2):
    a = (p1[0] - p2[0] + 1) * (p1[1] - p2[1] + 1)
    if a > 0:
        return a
    return -a

def part_1(data):
    max_area = 0
    for i, p1 in enumerate(data):
        for j in range(i+1, len(data)):
            area = get_area(p1, data[j])
            if area > max_area:
                max_area = area
    return max_area



class none_of_this_works_and_i_just_dont_want_to_seeit:
    # for each new bit of data,
    # loop through the current x's in the loop
    # if it's a new one, add in the new values and check if there is ones either side of it 
    # which need to be accounted for in the new value
    # ie when doing the first half of the loop, it should be as if you're adding in all the x values
    # so there is no 'new' ones for the bottom half.

    # need to check:
    #   p is greater than x
    #   p is less than the next x
    #   and not go past the end of the list

    # check if p is a new largest
    # so will always have x larger than it after that
    def make_loop(data):
        xs = [data[0][0]]
        y_ranges = [(data[0][1])]
        for px, py in data[1:]:
            # new smallest element
            if px < xs[0]:
                xs.insert(0, )
            # new largest element
            elif px > xs[-1]:
                xs += [px]
                y_ranges += [[py]]
            
            elif px in xs:
                i = xs.index(px)
                new_list = sorted(y_ranges[i] + [px[1]])
                y_ranges[i] = [new_list[0], new_list[-1]]
        
            # p isn't smallest, largest, or in xs, so need to find it's place in the list
            for i, x in enumerate(xs):
                if px > x:
                    continue
                elif px < x: # should be able to just make this an else statement
                    xs.insert(i, px)
                    ys_left = y_ranges[i-1]
                    ys_right = y_ranges[i]

                    break
                else:
                    raise ValueError("should've found a spot for p by now")


    def old_make_loop(data):
        # this doesn't work ... 
        # loop is dict with x value as the key the [min_y, max_y] for the value
        loop = dict()
        for p in data:
            x, y = p
            xs = list(loop.keys())
            if x not in loop:
                loop[x] = y
                continue

            l_ys = loop[x]
            if isinstance(l_ys, int):
                loop[x] = sorted([y, l_ys])
                continue
            if y < l_ys[0]:
                loop[x] = [y, l_ys[1]]
            elif y > l_ys[1]:
                loop[x] = [l_ys[0], y]

        return dict(sorted(loop.items()))


    def ys_in_loop(loop_ys, rect_ys):
        if loop_ys[0] <= rect_ys[0] and loop_ys[1] >= rect_ys[1]:
            return True
        return False

    def rect_in_loop(loop: dict, p1, p2):
        xs = list(loop.keys())
        rect_xs = sorted([p1[0], p2[0]])
        rect_ys = sorted([p1[1], p2[1]])
        for i, x in enumerate(xs):
            # not reached the start of the rect yet
            if x < rect_xs[0]:
                continue
            # passing the end of the rect
            elif x >= rect_xs[1]:
                if ys_in_loop(loop[x], rect_ys):
                    return True
            # first crossing onto rect so need to check x before
            elif xs[i-1] < rect_xs[0] and x != rect_xs[0]:
                if not ys_in_loop(loop[xs[i-1]], rect_ys):
                    return False
            # checking for current x's
            elif not ys_in_loop(loop[x], rect_ys):
                return False


    def part_2(data):
        data = np.array(data)
        print(data)
        plt.plot(data[:,0], data[:,1])
        plt.show()
        # max_area = 0
        # loop = make_loop(data)
        return
        for i, p1 in enumerate(data):
            for j in range(i+1, len(data)):
                p2 = data[j]
                area = get_area(p1, p2)
                if area > max_area:
                    if rect_in_loop(loop, p1, p2):
                        max_area = area

def part_2(data):
    ...
# could try testing to see if any of the lines intersect with the rectangles lines
# and a check to see if it is completely outside the shape
# but still running into how do I know if its completely outside...
# 
# could try and find a convex hull algo or something
# 
# could just make a list of all allowed points, but that seems like it would also be difficult  

if __name__ == "__main__":

    with open(path + f"/9.txt", "r") as f:
    # with open(path + f"/test.txt", "r") as f:
        data = f.readlines()
        f.close()
    data = [list(map(int, s.split(","))) for s in data]

    # print(part_1(data))
    print(part_2(data))
    
    # submit(part_1(data), session=session, day=9)
