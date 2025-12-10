
import sys
from aocd.post import submit
from typing import List
import numpy as np


path =  sys.path[0]
sys.path.append("..")

with open("session.txt", "r") as s:
    session = s.read()
    s.close()
    

def parse_data(data):
    return [list(map(int, s.split(','))) for s in data]

def dist_sqrd(p_1, p_2):
    return (p_1[0] - p_2[0])**2 + (p_1[1] - p_2[1])**2 + (p_1[2] - p_2[2])**2 


def get_distances(data):
    length = len(data)
    deltas = np.zeros((length, length), dtype=float)
    for i, p1 in enumerate(data):
        for j in range(i+1, length):
            deltas[i, j] = dist_sqrd(p1, data[j])
    return deltas


def make_networks(delta_matrix, connection_number):
    distances = np.sort(delta_matrix[delta_matrix != 0.0])[:connection_number]
    networks = []
    for d in distances:
        connection = np.where(delta_matrix == d)
        connection = [connection[0][0], connection[1][0]]

        in_net = -1 # using -1 instead of false so it works for the first element of the list
        for i, net in enumerate(networks):
            c0 = connection[0] in net
            c1 = connection[1] in net

            if c0 or c1:
                if in_net == -1:
                    in_net = i
                    if not c0:
                        networks[i] += [connection[0]]
                    elif not c1:
                        networks[i] += [connection[1]]
                        
                else:
                    networks[in_net] = list(set(networks[in_net]).union(net))
                    networks.remove(net)
                    break # shouldn't  be able to match more than twice

        if in_net == -1:
            networks += [connection]

    return sorted(networks, key=len)[::-1]


def part_1(data):
    data = parse_data(data)
    length = len(data)
    deltas = get_distances(data)
    networks = make_networks(deltas, length)
    result = 1
    for n in networks[:3]:
        result *= len(n)

    return result


def part_2(data):
    ...


if __name__ == "__main__":

    with open(path + f"/8.txt", "r") as f:
        data = f.readlines()
        f.close()

    print(part_1(data))
    # print(part_2(data))
    
    # submit(part_1(data), session=session, day=8)
