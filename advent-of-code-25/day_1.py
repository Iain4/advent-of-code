


def directioned_input(input:str):
    d, n = input[0], int(input[1:])
    if d == "R":
        return n
    return -n



def part_1(data):
    
    dial_value = 50 # starting position
    zeros_count = 0

    for val in data:
        dial_value += directioned_input(val)
        dial_value = dial_value % 100

        if dial_value == 0:
            zeros_count += 1
    print(zeros_count)




def direc_and_input(input:str):
    d, n = input[0], int(input[1:])
    if d == "R":
        return 1, n
    return -1, n


def sign(value):
    if value > 0:
        return 1
    elif value < 0:
        return -1
    return None


def part_2(data):

    dial_value = 50
    zero_passes = 0

    for val in data:
        sign_before = sign(dial_value)
        d, n = direc_and_input(val)

        if n / 100 >= 1:
            zero_passes += int(n / 100) # int rounds down 

        dial_value += d * (n % 100)

        if dial_value == 0:
            zero_passes += 1
        elif sign_before != sign(dial_value) and sign_before != None:
            zero_passes += 1
        elif dial_value >=100 or dial_value <= -100:
            zero_passes += 1

        dial_value = dial_value % 100
    
    print(zero_passes)


if __name__ == "__main__":
    with open("advent-of-code-25/1.txt", "r") as f:
        data = f.read().splitlines()
        f.close()

    part_2(data)