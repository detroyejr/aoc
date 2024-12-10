"""Day 10"""

import itertools
import operator


def puzzle_input(file):
    with open(file, "r+") as file:
        x = list(map(str.strip, file.readlines()))
        return list(map(lambda x: list(map(int, x)), x))


def value_at(x, position):
    i, j = position
    return x[i][j]


def valid_location(x, current, position, coordinates):
    return position in coordinates and value_at(x, current) + 1 == value_at(x, position)


def move(position, movement):
    return tuple(itertools.starmap(operator.add, zip(position, movement)))


def piece1(x, position, coordinates, seen=set()):
    movements = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
    ]

    if value_at(x, position) == 9:
        seen.add(position)
        return

    for movement in movements:
        move_location = move(position, movement)
        if valid_location(x, position, move_location, coordinates):
            piece1(x, move_location, coordinates, seen)

    return seen


def piece2(x, position, coordinates, seen=list()):
    movements = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
    ]

    if value_at(x, position) == 9:
        seen.append(position)
        return

    for movement in movements:
        move_location = move(position, movement)
        if valid_location(x, position, move_location, coordinates):
            piece2(x, move_location, coordinates, seen)

    return seen


def part1(x):
    """
    >>> x = '''
    ... 89010123
    ... 78121874
    ... 87430965
    ... 96549874
    ... 45678903
    ... 32019012
    ... 01329801
    ... 10456732
    ... '''.strip().splitlines()
    >>> x = list(map(lambda x: list(map(int, x)), x))
    >>> part1(x)
    36
    """
    coordinates = [(i, j) for i in range(len(x)) for j in range(len(x))]
    trailheads = [(i, j) for i, j in coordinates if x[i][j] == 0]
    return sum([len(piece1(x, head, coordinates, set())) for head in trailheads])


def part2(x):
    """
    >>> x = '''
    ... 89010123
    ... 78121874
    ... 87430965
    ... 96549874
    ... 45678903
    ... 32019012
    ... 01329801
    ... 10456732
    ... '''.strip().splitlines()
    >>> x = list(map(lambda x: list(map(int, x)), x))
    >>> part2(x)
    81
    """
    coordinates = [(i, j) for i in range(len(x)) for j in range(len(x))]
    trailheads = [(i, j) for i, j in coordinates if x[i][j] == 0]
    return sum([len(piece2(x, head, coordinates, list())) for head in trailheads])


if __name__ == "__main__":
    x = puzzle_input("inputs/10.txt")
    print("Part 1:", part1(x))
    print("Part 2:", part2(x))
