from typing import List
from collections import deque

def sim(counts: List[int], n: int):
    for _ in range(n):
        new_fish = counts[0]
        counts = counts[1:] + counts[:1]
        counts[6] += new_fish
    return counts


if __name__ == "__main__":
    counts = [0] * 9
    with (open("day6/input.txt", "r")) as f:
        for d in [int(x) for x in f.read().split(",")]:
            counts[d] += 1

    print(sum(sim(counts.copy(), 80)))
    print(sum(sim(counts.copy(), 256)))
