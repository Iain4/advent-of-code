# from aocd.post import submit
# from getData import session

with open('4.txt', 'r') as f:
    data = f.read().splitlines()
    f.close()

### PART 1 ###
def part_1(data:list) -> int:
    total = 0
    for row in data:
        row = row.split(': ')[1]
        wins, ours = row.split(' | ')
        wins, ours = wins.split(' '), ours.split(' ')
        num_wins = -1
        for n in ours:
            if n == '':
                continue
            elif n in wins:
                num_wins += 1
        if num_wins >= 0:
            total += 2**num_wins
    return total

### PART 2 ###
def part_2(data:list) -> int:
    # initializes the data
    # makes the first item in the list for each row the number of copies of that card
    for n, row in enumerate(data):
        row = row.split(': ')
        row[0] = 1
        data[n] = row
    
    for n, row in enumerate(data):
        num_wins = find_wins(row[1])
        if num_wins > 0:
            data = propegate_copies(data, n, num_wins)

    total = 0
    for row in data:
        total += row[0]
    return total

def find_wins(row_data:str) -> int:
    # finds how many wins a given card has
    num_wins = 0
    wins, ours = row_data.split(' | ')
    wins, ours = wins.split(' '), ours.split(' ')
    num_wins = 0
    for n in ours:
        # need this cause theres 2 spaces for single digit numbers
        if n == '':
            continue
        elif n in wins:
            num_wins += 1
    return num_wins

def propegate_copies(data:list, row_number:int, num_wins:int) -> list:
    copies = data[row_number][0]
    for i in range(row_number+1, row_number+num_wins+1):
        data[i][0] += copies
    return data

# total_1 = part_1(data)
# print(total_1)
total_2 = part_2(data)
# print(total_2)
# submit(total_2, session=session)