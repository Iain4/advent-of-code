from getData import session
from aocd.post import submit

with open('3.txt', 'r') as f:
    data = f.read()
    f.close()

data = data.splitlines()

### PART 1 ###
def find_nums(row: str) -> list:
    nums = []
    i = 0
    while i < len(row):
        if row[i].isdigit():
            start = i
            end = i+1
            while i < len(row):
                if not row[i].isdigit():
                    break
                i += 1
                end = i
            val = int(row[start:end])
            nums += [(val, (start, end))]
        i += 1
    return nums

def check_for_symbol(data: list, row_num: int, num_points: tuple) -> bool:
    # checks if a symbol is around the number
    start = num_points[0] - 1
    if start < 0:
        start = 0
    end = num_points[1] + 1
    if end > len(data[row_num]):
        end = len(data[row_num])

    try:
        if row_num == 0:
            check_rows = data[row_num:row_num+2]
        else:
            check_rows = data[row_num-1:row_num+2]
    except IndexError:
        check_rows = data[row_num-1:]

    for row in check_rows:
        for char in row[start:end]:
            if char == '.':
                pass
            else:
                if not char.isdigit():
                    return True
    return False

def part_1(data: list):# -> int:
    total = 0

    for i, row in enumerate(data):
        nums = find_nums(row)
        for n in nums:
            if check_for_symbol(data, i, n[1]):
                total += n[0]
    return total

### PART 2 ###



answer_1 = part_1(data)
print(answer_1)
# submit(
#     session=session,
#     answer=answer_1
# )