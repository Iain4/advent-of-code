from aocd import get_data

# session = "session_token" # work laptop
session = "session_token" # pc

filename = "5.txt"

data = get_data(day=5, year=2023, session=session)

with open(filename, "w") as f:
    f.write(data)
    f.close()