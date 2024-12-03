"""Day 2"""

import itertools


def puzzle_input(file):
    with open(file, "r+") as file:
        return [r.strip().split(" ") for r in file.readlines()]


def piece1(x):
    xi = map(int, x)
    pairs = list(itertools.pairwise(xi))
    greater_than_last = itertools.starmap(lambda x, y: x > y, pairs)
    less_than_last = itertools.starmap(lambda x, y: x < y, pairs)
    difference_between_zero_four = itertools.starmap(
        lambda x, y: 0 < abs(x - y) < 4, pairs
    )
    return (all(greater_than_last) or all(less_than_last)) and all(
        difference_between_zero_four
    )


def piece2(x):
    p1 = piece1(x)
    if p1:
        return True
    for i in range(len(x)):
        xc = x.copy()
        xc.pop(i)
        if piece1(xc):
            return True
    return False


def part1(x):
    """
    >>> part1([
    ...     [8,6,4,2,1],
    ...     [1,2,7,8,9],
    ...     [9,7,6,2,1],
    ...     [1,3,2,4,5],
    ...     [8,6,4,4,1],
    ...     [1,3,6,7,9]
    ... ])
    2
    """
    return sum(map(piece1, x))


def part2(x):
    """
    >>> part2([
    ...     [8,6,4,2,1],
    ...     [1,2,7,8,9],
    ...     [9,7,6,2,1],
    ...     [1,3,2,4,5],
    ...     [8,6,4,4,1],
    ...     [1,3,6,7,9]
    ... ])
    4
    """
    return sum(map(piece2, x))


if __name__ == "__main__":
    x = puzzle_input("inputs/02.txt")
    print("Part 1:", part1(x))
    print("Part 2:", part2(x))
