from aocd import get_data

session = "session_token"

filename = "1.txt"

data = get_data(day=1, year=2025, session=session)

with open(filename, "w") as f:
    f.write(data)
    f.close()