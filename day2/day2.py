from pprint import pprint

"""
forward X increases the horizontal position by X units.
down X increases the depth by X units.
up X decreases the depth by X units.
"""


class Vec2:
    x: int
    y: int

    def __repr__(self) -> str:
        return f"{self.x}, {self.y} -- {self.x * self.y}"


def part1():
    pos = Vec2()
    pos.x = 0
    pos.y = 0

    with open("day2/input.txt") as f:
        for line in f:
            ops = line.split()
            print(ops)
            if ops[0] == "forward":
                pos.x += int(ops[1])
            elif ops[0] == "down":
                pos.y += int(ops[1])
            elif ops[0] == "up":
                pos.y -= int(ops[1])

    return pos


def part2():
    pos = Vec2()
    pos.x = 0
    pos.y = 0

    aim = 0

    with open("day2/input.txt") as f:
        for line in f:
            ops = line.split()
            print(ops)
            if ops[0] == "forward":
                pos.x += int(ops[1])
                pos.y += aim * int(ops[1])
            elif ops[0] == "down":
                aim += int(ops[1])
            elif ops[0] == "up":
                aim -= int(ops[1])

    return pos


if __name__ == "__main__":
    pprint(part1())
    pprint(part2())
