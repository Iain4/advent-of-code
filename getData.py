import aocd

# session = "session_token" # work laptop
session = "session_token" # pc

filename = "3.txt"

data = aocd.get_data(day=3, year=2023, session=session)

with open(filename, "w") as f:
    f.write(data)
    f.close()