
def id_invalid_p1(id:int):
    id = str(id)
    length = len(id)
    
    if length % 2 == 1:
        return False
    
    half = int(length / 2)
    if id[:half] == id[half:]:
        return True
    
    return False

def part_1(ID_ranges):
    invalid_id_sum = 0

    for idr in ID_ranges:
        lens = [len(id) for id in idr]

        # skipping ranges with only odd lengths
        if lens[0] == lens[1] and lens[0] % 2 == 1: 
            continue
        
        id = int(idr[0])
        while id <= int(idr[1]):

            # itterating to the next id with an even length
            if len(str(id)) % 2 == 1:
                id = 10 ** len(str(id))
                continue
            
            if id_invalid_p1(id):
                invalid_id_sum += id
        
            id += 1
    
    print(invalid_id_sum)
            


def id_invalid_p2(id:str):
    length = len(id)
    half = int(length / 2)
    
    for i in range(1,half+1):
        # seeing if that repeating number can fit
        if length % i != 0:
            continue
        
        repeats = int(length / i)
        if id[:i] * repeats == id:
            return True
    
    return False


def part_2(ID_ranges):
    invalid_id_sum = 0

    for idr in ID_ranges:
        start, stop = idr
        start, stop = int(start), int(stop)+1

        for id in range(start, stop):
            if id_invalid_p2(str(id)):
                invalid_id_sum += id

    print(invalid_id_sum)


if __name__ == "__main__":
    with open("advent-of-code-25/2.txt") as f:
        data = f.read()

    ID_ranges = [s.split("-") for s in data.split(",")]

    part_2(ID_ranges)