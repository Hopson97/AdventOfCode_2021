import statistics
import math
from typing import Deque

with open("day7/input.txt") as f:
    # read list of numbers separated by , into a list of ints
    numbers = [int(x) for x in f.read().split(",")]

med = int(statistics.median(numbers))

fuel = 0
for position in numbers:
    fuel += abs(position - med)
print(fuel)


def gauss(x):
    return (x * (1 + x)) / 2


minpos = min(numbers)
maxpos = max(numbers)

fuel_min = 9999999999999999999999999
for i in range(minpos, maxpos):
    fuel = 0

    for position in numbers:
        fuel += gauss(abs(i - position))

    fuel_min = min(fuel, fuel_min)
print(fuel_min)
