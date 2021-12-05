from pprint import pprint
from typing import Dict, List

def idx(x,y):
    return x + y * 5

def get_grids():
    guesses = []
    grids = []

    current_grid = []
    with open("day4/input.txt", "r") as f:
        for i, line in enumerate(f):
            line = line.strip()
            if i == 0:
                guesses = [int(x) for x in line.split(",")]
            elif len(line) == 0:
                if current_grid:
                    grids.append({"ns": current_grid,"found": [False] * 25  })
                current_grid = []
            else:
                current_grid += [int(x) for x in line.split()]
    return guesses, grids


def part1():
    guesses, grids = get_grids()
    for guess in guesses:
        for grid in grids:
            for i, n in enumerate(grid["ns"]):
                if n == guess:
                    grid["found"][i] = True

            for y in range(5):
                for x in range(5):
                    if not grid["found"][idx(x, y)]:
                        break
                else:
                    s = sum(n for i, n in enumerate(grid["ns"]) if not grid["found"][i])
                    print(guess, s)

                    return guess * s
            for x in range(5):
                for y in range(5):
                    if not grid["found"][idx(x, y)]:
                        break
                else:
                    s = sum(n for i, n in enumerate(grid["ns"]) if not grid["found"][i])

                    print(guess, s)
                    return guess * s



if __name__ == '__main__':
    print(part1())