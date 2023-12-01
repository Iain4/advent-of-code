import aocd

session = "session_token"
filename = "1a.txt"

data = aocd.get_data(day=1, year=2023, session=session)

with open(filename, "w") as f:
    f.write(data)
    f.close()