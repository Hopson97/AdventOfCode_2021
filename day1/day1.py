# https://adventofcode.com/2021/day/1
#


def part1():
    """
    Counts the number of numerical increases in the input file
    """
    prev = 999999999999999999
    count = 0

    #
    with open("day1/input.txt", "r") as f:
        for line in f:
            if int(line) > prev:
                count += 1
            prev = int(line)
    return count


def part2():
    """
    Sums the previous 3 numbers in the input file and counts the number of sum increases
    """
    # Store all previous sums of 3 numbers
    prev = []

    # Store the current sum of 3 numbers
    sums = []

    # Store the current number of increases
    count = 0
    with open("day1/input.txt", "r") as f:
        for line in f:
            prev.append(int(line))

            # When there are at least 3 previous numbers,
            # sum the last 3 numbers and see if the sum is
            # greater than the sum of the previous 3 numbers
            if len(prev) > 2:
                sums.append(sum(prev[-3:]))
                if len(sums) > 1 and sums[-1] > sums[-2]:
                    count += 1
    return count


if __name__ == "__main__":
    count = part1()
    print(count)

    print(part2())
