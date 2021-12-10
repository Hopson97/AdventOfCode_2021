from time import sleep

WIDTH = 100
HEIGHT = 100
data = []
with open("day9/input.txt") as f:
    for line in f:
        for c in line.strip():
            data.append(int(c))


def get_height(x, y):
    if x < 0 or y < 0 or x >= WIDTH or y >= HEIGHT:
        return 99999999

    return data[x + y * WIDTH]


sums = 0
for y in range(HEIGHT):
    for x in range(WIDTH):
        val = get_height(x, y)
        if (
            get_height(x + 1, y) > val
            and get_height(x - 1, y) > val
            and get_height(x, y + 1) > val
            and get_height(x, y - 1) > val
        ):
            sums += val + 1



def flood_basin(count, x, y, visited):

    if x < 0 or y < 0 or x >= WIDTH or y >= 100:
        return count

    if get_height(x, y) >= 9:
        return count

    if (x, y) in visited:
        return count

    count += 1

    visited[(x, y)] = True

    count = flood_basin(count, x + 1, y, visited)
    count = flood_basin(count, x - 1, y, visited)
    count = flood_basin(count, x, y + 1, visited)
    count = flood_basin(count, x, y - 1, visited)
    return count


counts = []
for y in range(HEIGHT):
    for x in range(WIDTH):
        val = get_height(x, y)
        if (
            get_height(x + 1, y) > val
            and get_height(x - 1, y) > val
            and get_height(x, y + 1) > val
            and get_height(x, y - 1) > val
        ):
            counts.append(flood_basin(0, x, y, {}))

sums = 1
counts.sort()
counts.reverse()
print(counts[:3])
for count in counts[:3]:
    sums *= count

print(sums)