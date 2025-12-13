from aocd.post import submit
# from getData import session

with open("2.txt", "r") as f:
    data = f.read()
    f.close()

# data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

data = data.splitlines()


### PART 1 ###
def part_1(data):
    max_colours_vals = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    total = 0
    for n, game in enumerate(data):
        game = game.split(": ")[1]
        hands = game.split("; ")
        
        game_works = True
        for hand in hands:
            hand = hand.split(', ')

            for colour in hand:
                colour = colour.split(' ')

                if int(colour[0]) > max_colours_vals[colour[1]]:
                    game_works = False
                    break
            if not game_works:
                break

        if game_works:
            total += n+1

    return total


### PART 2 ###
def part_2(data):
    total = 0

    for game in data:
        game = game.split(": ")[1]
        hands = game.split("; ")

        min_possible_vals = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        
        for hand in hands:
            hand = hand.split(', ')

            for colour in hand:
                colour = colour.split(' ')

                if int(colour[0]) > min_possible_vals[colour[1]]:
                    min_possible_vals[colour[1]] = int(colour[0])
        
        x=1
        for key in min_possible_vals:
            if min_possible_vals[key] == -1:
                continue
            x = x*min_possible_vals[key]
        total += x

    return total

total_1 = part_1(data)
total_2 = part_2(data)
print(f'{total_1 = } \n{total_2 = }')
submit(
    answer=total_2,
    session=session
)
