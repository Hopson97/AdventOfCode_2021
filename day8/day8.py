def p1():
    s = 0
    with open("day8/input.txt", "r") as f:
        for line in f:
            line = line.strip().split("|")
            outputs = line[1].split()
            for output in outputs:
                if len(output) in [2, 4, 3, 7]:
                    s += 1
    return s


print(p1())
