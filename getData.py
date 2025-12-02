from aocd import get_data

day = 2

session = "session_token"

filename = f"{day}.txt"

data = get_data(day=day, year=2025, session=session)

with open(filename, "w") as f:
    f.write(data)
    f.close()