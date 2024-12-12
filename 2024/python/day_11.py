"""Day 11"""

import functools


def puzzle_input(file):
    return open(file, "r+").read().strip().split(" ")


def stones(x):
    if x == "0":
        return ("1", None)
    elif len(x) % 2 == 0:
        n = int(len(x) / 2)
        return (x[:n], str(int(x[n:])))
    else:
        return (str(int(x) * 2024), None)


@functools.cache
def piece1(x, blink):
    if not x:
        return 0
    if blink == 0:
        return 1
    left, right = stones(x)
    return piece1(left, blink - 1) + piece1(right, blink - 1)


def part1(x, blinks):
    return sum([piece1(x, blinks) for x in x])


def part2(x, blinks):
    return sum([piece1(x, blinks) for x in x])


if __name__ == "__main__":
    x = puzzle_input("inputs/11.txt")
    print("Part 1:", part1(x, 25))
    print("Part 1:", part2(x, 75))
