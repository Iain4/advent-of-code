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
def part_2(data: list) -> list:
    # returns list of tuples of:
    # (value, (star's index in data))
    star_nums = []
    star_pos = []
    for n, row in enumerate(data):
        nums = find_nums(row)
        for num in nums:
            star = check_for_star(data, n, num[1])
            if star:
                star_nums += [(num[0], star)]
                star_pos += [star]

    total = 0
    for i in range(len(star_nums)-1):
        num_1 = star_nums[i]
        for j in range(i+1, len(star_nums)):
            num_2 = star_nums[j]
            if num_1[1] == num_2[1]:
                total += num_1[0] * num_2[0]
    return total

def check_for_star(data: list, row_num: int, num_points: tuple) -> bool:
    # checks if a symbol is around the number
    start = num_points[0] - 1
    if start < 0:
        start = 0
    end = num_points[1] + 1
    if end > len(data[row_num]):
        end = len(data[row_num])

    if row_num == 0:
        row_nums = range(row_num,row_num+2)
    elif row_num+2 >= len(data[row_num]):
        row_nums = range(row_num-1, len(data[row_num]))
    else:
        row_nums = range(row_num-1,row_num+2)

    for i in row_nums:
        row = data[i]
        for j, char in enumerate(row):
            if char == '*' and j in range(start,end):
                return True, (i,j)
    return False

answer_1 = part_1(data)
print(answer_1)

answer_2 = part_2(data)
print(answer_2)

# submit(
#     session=session,
#     answer=answer_2
# )