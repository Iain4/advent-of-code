from aocd.post import submit
import pstats
import cProfile

def getFirstNum(string):
    for n, s in enumerate(string):
        if s.isdigit():
            return n
    return len(string)

def findTxtNum(string, reversed=False):
    txt_nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(string)-5):
        s = string[i: i+5]
        for n, num in enumerate(txt_nums):
            if reversed:
                num = num[::-1]
            if num in s:
                return str(n+1)
    return None

def main():
    with open("1.txt", "r") as f:
        data = f.read().splitlines()
        f.close()

#     data = '''two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen'''.splitlines()

    result = 0

    for row in data:
        pos = getFirstNum(row)
        ret = findTxtNum(row[:pos])
        if ret is not None:
            A = ret
        else:
            A = row[pos]

        row = row[::-1]
        pos = getFirstNum(row)
        ret = findTxtNum(row[:pos], reversed=True)
        if ret is not None:
            B = ret
        else:
            B = row[pos]

        result += int(A+B)    

    print(result)
    # submit(
    #     answer=result,
    #     session="53616c7465645f5f186878039ece58656365c1cc38126c25e88a97b152f885ef325d90ac8bda874c1190ed8f55318bdc6283e260ec9f17a3aacc76d326318206"
    # )

if __name__ == "__main__":
    with cProfile.Profile() as pr:
        main()
    
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats(10)