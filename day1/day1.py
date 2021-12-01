

def part1():
    """
    >>> part1()
    """
    prev = 999999999999999999
    count = 0
    with open ("day1/input.txt", "r") as f:
        for line in f:        
            if int(line) > prev:
                count += 1
            prev = int(line)
    return count

def part2():
    prev = []
    sums = []
    count = 0
    with open ("day1/input.txt", "r") as f:
        for line in f:        
            v = int(line)
            prev.append(v)

            #sum the last 3 values in 'prev'
            if len(prev) > 2:
                sums.append(sum(prev[-3:]))
                if len(sums) > 1 and sums[-1] > sums[-2]:
                    count += 1
    return count



if __name__ == '__main__':
    count = part1()
    print(count)

    print(part2())