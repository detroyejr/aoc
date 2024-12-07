"""Day 7"""

import itertools
import operator


def puzzle_input(file):
    with open(file, "r+") as file:
        x = list(map(str.strip, file.readlines()))
        x = map(str.split, x, [":"] * len(x))
        return [
            (int(target), list(map(int, numbers.strip().split(" "))))
            for target, numbers in x
        ]


def calculate(batch, f):
    i, j = batch[0]
    return itertools.chain([f(i, j)], *batch[1:])


def concat(i, j):
    return int(operator.add(str(i), str(j)))


def piece1(target, x):
    if len(x) == 1:
        return sum(x) == target
    batch = list(itertools.batched(x, 2))
    adds = list(calculate(batch, operator.add))
    multiplies = list(calculate(batch, operator.mul))
    if piece1(target, adds) or piece1(target, multiplies):
        return True
    return False


def piece2(target, x):
    if len(x) == 1:
        return sum(x) == target
    batch = list(itertools.batched(x, 2))
    adds = list(calculate(batch, operator.add))
    multiplies = list(calculate(batch, operator.mul))
    concats = list(calculate(batch, concat))
    if piece2(target, adds) or piece2(target, multiplies) or piece2(target, concats):
        return True
    return False


def part1(x):
    """
    >>> x = [
    ...  (190, [10, 19]),
    ...  (3267, [81, 40, 27]),
    ...  (83, [17, 5]),
    ...  (156, [15, 6]),
    ...  (7290, [6, 8, 6, 15]),
    ...  (161011, [16, 10, 13]),
    ...  (192, [17, 8, 14]),
    ...  (21037, [9, 7, 18, 13]),
    ...  (292,[11, 6, 16, 20]),
    ... ]
    >>> part1(x)
    3749
    """
    return sum([target for target, x in x if piece1(target, x)])


def part2(x):
    """
    >>> x = [
    ...  (190, [10, 19]),
    ...  (3267, [81, 40, 27]),
    ...  (83, [17, 5]),
    ...  (156, [15, 6]),
    ...  (7290, [6, 8, 6, 15]),
    ...  (161011, [16, 10, 13]),
    ...  (192, [17, 8, 14]),
    ...  (21037, [9, 7, 18, 13]),
    ...  (292,[11, 6, 16, 20]),
    ... ]
    >>> part2(x)
    11387
    """
    return sum([target for target, x in x if piece2(target, x)])


if __name__ == "__main__":
    x = puzzle_input("inputs/07.txt")
    print("Part 1:", part1(x))
    print("Part 2:", part2(x))
