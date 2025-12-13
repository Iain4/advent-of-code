from aocd import get_data
from boilerplate import boilerplate

path = "./advent-of-code-25/"
day = 11


def main():
    with open("session.txt", "r") as f:
        session = f.read()
        f.close()

    data_filename = path + f"{day}.txt"
    code_filename = path + f"day_{day}.py"

    data = get_data(day=day, year=2025, session=session)

    with open(data_filename, "w") as f:
        f.write(data)
        f.close()

    with open(code_filename, "w") as f:
        f.write(boilerplate(day, path))
        f.close()


if __name__ == "__main__":
    main()