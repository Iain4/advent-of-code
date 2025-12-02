


def directioned_input(input:str):
    d, n = input[0], int(input[1:])
    if d == "R":
        return n
    return -n



def main():
    with open("advent-of-code-25/1.txt", "r") as f:
        data = f.read().splitlines()
        f.close()
    
    dial_value = 50 # starting position
    zeros_count = 0

    for val in data:
        dial_value += directioned_input(val)
        dial_value = dial_value % 100

        if dial_value == 0:
            zeros_count += 1
    print(zeros_count)

if __name__ == "__main__":
    main()