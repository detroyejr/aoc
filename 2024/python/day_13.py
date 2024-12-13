"""Day 13"""

import re
import itertools


def puzzle_input(file):
    with open(file, "r+") as f:
        x = re.sub("\\s{2,}", "\n", f.read())
        x = x.strip().splitlines()
        x = [x for x in x if x]
        return list(itertools.batched(x, 3))


def button_group(x):
    x[0].splitlines()


def calc(a, b, prize):
    return (prize - (a * x)) / b


def piece1(a, b, prize):
    x1, y1 = re.findall("\\d+", a)
    x2, y2 = re.findall("\\d+", b)
    p1, p2 = re.findall("\\d+", prize)

    def f(x1, x2, y1, y2, p1, p2):
        return (int(p2) * int(x2) - int(p1) * int(y2)) / (
            int(x2) * int(y1) - int(x1) * int(y2)
        )

    x, y = f(x1, x2, y1, y2, p1, p2), f(x2, x1, y2, y1, p1, p2)

    if x == int(x) and y == int(y):
        return x * 3 + y
    return 0


def piece2(a, b, prize):
    x1, y1 = re.findall("\\d+", a)
    x2, y2 = re.findall("\\d+", b)
    p1, p2 = re.findall("\\d+", prize)
    p1, p2 = int(p1), int(p2)
    p1 += 1e13
    p2 += 1e13

    def f(x1, x2, y1, y2, p1, p2):
        return (int(p2) * int(x2) - int(p1) * int(y2)) / (
            int(x2) * int(y1) - int(x1) * int(y2)
        )

    x, y = f(x1, x2, y1, y2, p1, p2), f(x2, x1, y2, y1, p1, p2)

    if x == int(x) and y == int(y):
        return x * 3 + y
    return 0


def part1(x):
    """
    >>> x = '''
    ... Button A: X+94, Y+34
    ... Button B: X+22, Y+67
    ... Prize: X=8400, Y=5400
    ...
    ... Button A: X+26, Y+66
    ... Button B: X+67, Y+21
    ... Prize: X=12748, Y=12176
    ...
    ... Button A: X+17, Y+86
    ... Button B: X+84, Y+37
    ... Prize: X=7870, Y=6450
    ...
    ... Button A: X+69, Y+23
    ... Button B: X+27, Y+71
    ... Prize: X=18641, Y=10279
    ... '''
    >>> x = re.sub(r'\\s{2,}', r'\\n', x)
    >>> x = x.strip().splitlines()
    >>> x = list(itertools.batched(x, 3))
    >>> part1(x)
    480
    """

    return int(sum([piece1(*x) for x in x if x]))


def part2(x):
    """
    >>> x = '''
    ... Button A: X+94, Y+34
    ... Button B: X+22, Y+67
    ... Prize: X=8400, Y=5400
    ...
    ... Button A: X+26, Y+66
    ... Button B: X+67, Y+21
    ... Prize: X=12748, Y=12176
    ...
    ... Button A: X+17, Y+86
    ... Button B: X+84, Y+37
    ... Prize: X=7870, Y=6450
    ...
    ... Button A: X+69, Y+23
    ... Button B: X+27, Y+71
    ... Prize: X=18641, Y=10279
    ... '''
    >>> x = re.sub(r'\\s{2,}', r'\\n', x)
    >>> x = x.strip().splitlines()
    >>> x = list(itertools.batched(x, 3))
    >>> part2(x)
    875318608908
    """
    return int(sum([piece2(*x) for x in x if x]))


if __name__ == "__main__":
    x = puzzle_input("inputs/13.txt")
    print("Part 1:", part1(x))
    print("Part 2:", part2(x))
