def get_input():
    map = {}
    with open("day5/input.txt") as f:
        for line in f:
            vals = line.replace("->", "").split()
            from_pos = vals[0].split(",")
            from_pos = (int(from_pos[0]), int(from_pos[1]))
            to_pos = vals[1].split(",")
            to_pos = (int(to_pos[0]), int(to_pos[1]))

            if from_pos[0] == to_pos[0]:
                from_val = min(from_pos[1], to_pos[1])
                to_val = max(from_pos[1], to_pos[1])

                for y in range(from_val, to_val + 1):
                    pos = f"{from_pos[0]},{y}"
                    if pos not in map:
                        map[pos] = 0
                    map[pos] += 1

            elif from_pos[1] == to_pos[1]:
                from_val = min(from_pos[0], to_pos[0])
                to_val = max(from_pos[0], to_pos[0])

                for x in range(from_val, to_val + 1):
                    pos = f"{x},{from_pos[1]}"
                    if pos not in map:
                        map[pos] = 0
                    map[pos] += 1
    x = 0
    for k, v in map.items():
        if v > 1:
            x += 1
    return x


def part1():
    return get_input()


if __name__ == "__main__":
    print(part1())
