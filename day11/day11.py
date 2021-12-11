from typing import List, Dict, Tuple
from time import sleep

_WIDTH = 10
_HEIGHT = 10


def index(x, y):
    return x + (y * _WIDTH)


def get_val(grid: List[int], x: int, y: int):
    if x < 0 or x >= _WIDTH or y < 0 or y >= _HEIGHT:
        return 0
    return grid[index(x, y)]


def increment(grid: List[int], x: int, y: int, flashed: Dict[Tuple[int, int], bool]):
    new_flash = 0
    if x < 0 or x >= _WIDTH or y < 0 or y >= _HEIGHT or (x, y) in flashed:
        return 0

    grid[index(x, y)] += 1

    if get_val(grid, x, y) > 9:

        flashed[(x, y)] = True
        grid[index(x, y)] = 0

        new_flash += 1
        new_flash += increment(grid, x + 1, y, flashed)
        new_flash += increment(grid, x - 1, y, flashed)
        new_flash += increment(grid, x, y + 1, flashed)
        new_flash += increment(grid, x, y - 1, flashed)
        new_flash += increment(grid, x + 1, y - 1, flashed)
        new_flash += increment(grid, x - 1, y + 1, flashed)
        new_flash += increment(grid, x + 1, y + 1, flashed)
        new_flash += increment(grid, x - 1, y - 1, flashed)
    return new_flash


def print_grid(grid: List[int]):
    for y in range(_HEIGHT):
        for x in range(_WIDTH):
            print(get_val(grid, x, y), end=", ")
        print()
    print()


def get_grid() -> List[int]:
    grid = []
    with open("day11/input.txt") as f:
        for line in f:
            for char in line.strip():
                grid.append(int(char))
    return grid


def do_sim(grid: List[int], steps: int, find_big_flash: bool = False) -> int:
    flashes = 0

    for step in range(steps):
        flashed = {}
        for y in range(_HEIGHT):
            for x in range(_WIDTH):
                flashes += increment(grid, x, y, flashed)
                if find_big_flash and len(flashed.keys()) == 100:
                    return step
    return flashes


def part1() -> int:
    grid = get_grid()
    return do_sim(grid, 100)


def part2() -> int:
    grid = get_grid()
    return do_sim(grid, 100000, find_big_flash=True) + 1


if __name__ == "__main__":
    print(part1())
    print(part2())
