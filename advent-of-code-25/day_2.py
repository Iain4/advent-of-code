

def id_invalid(id:int):
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
            
            if id_invalid(id):
                invalid_id_sum += id
        
            id += 1
    
    print(invalid_id_sum)
            


# check if the id has an even number of values
# if it does, are both halves the same
# if not an even length, should itterate to one so not testing hunners of useless values.



if __name__ == "__main__":
    with open("advent-of-code-25/2.txt") as f:
        data = f.read()

    ID_ranges = [s.split("-") for s in data.split(",")]

    part_1(ID_ranges)