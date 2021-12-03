def part1():
    zeros = [0] * 12
    ones = [0] * 12

    with open("day3/input.txt") as f:
        for line in f:
            for i, n in enumerate(line.strip()):
                if n == "0":
                    zeros[i] += 1
                else:
                    ones[i] += 1

    gamma = "0b"
    epsilon = "0b"
    for zero, one in zip(zeros, ones):
        gamma += "0" if zero < one else "1"
        epsilon += "1" if zero < one else "0"

    gamma_n = int(gamma, 2)
    epsilon_n = int(epsilon, 2)
    return gamma_n * epsilon_n


def part2():
    ns = []
    with (open("day3/input.txt")) as f:
        ns = f.readlines()
    current_ox = ns.copy()
    current_co = ns.copy()

    def do_alg(l, bit, f):
        if len(l) == 1:
            return l
        zeros = []
        ones = []
        for n in l:
            if n[bit] == "0":
                zeros.append(n)
            else:
                ones.append(n)

        return f(zeros, ones)

    for i in range(len(ns[0])):
        current_ox = do_alg(
            current_ox, i, lambda zeros, ones: zeros if len(zeros) > len(ones) else ones
        )
        current_co = do_alg(
            current_co, i, lambda zeros, ones: ones if len(zeros) > len(ones) else zeros
        )

    return int(f"0b{current_ox[0]}", 2) * int(f"0b{current_co[0]}", 2)


if __name__ == "__main__":
    print(part1())

    print(part2())
