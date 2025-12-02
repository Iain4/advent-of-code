with open('5p.txt', 'r') as f:
    data = f.read()
    data = data.split('\n\n')

# destination start, source start, range

### PART 1 ###
def transform_with_map(inputs: list, map: str):
    map = [[int(x) for x in m.split()] for m in map.splitlines()[1:]]

    outputs = []
    for value in inputs:
        value_in_map = False
        for m in map:
            if m[1] <= value < m[1] + m[2]:
                outputs += [m[0] + value - m[1]]
                value_in_map = True
                break

        if not value_in_map:
            outputs += [value]
            
    return outputs

def part_1(data):
    input = [int(x) for x in data[0].split()[1:]]

    for map in data[1:]:
        input = transform_with_map(input, map)

    return min(input)

### PART 2 ###
# idk with part 2 yet
def transform_range_with_map(inputs: list, map: str) -> list:
    map = [[int(x) for x in m.split()] for m in map.splitlines()[1:]]
    for x in range(0, len(inputs), 2):
        ins = range(inputs[x], inputs[x+1])

        for m in map:
            dest_start, source_start, out_range = m
            sources = range(source_start, source_start+out_range)
            if all(ins in sources):



def part_2(data):
    seeds = [int(x) for x in data[0].split()[1:]]
    
    for map in data[1:]:
        inputs = transform_range_with_map(seeds, map)

    return min(inputs)

answer_1 = part_1(data)
print(f'part 1: {answer_1}')
answer_2 = part_2(data)
print(f'part 2: {answer_2}')

