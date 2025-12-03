from aocd import get_data

day = 3

with open("session.txt", "r") as f:
    session = f.read()
    f.close()

filename = f"{day}.txt"

data = get_data(day=day, year=2025, session=session)

with open(filename, "w") as f:
    f.write(data)
    f.close()