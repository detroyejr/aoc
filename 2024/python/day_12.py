"""Day 12"""

import itertools
import operator


def puzzle_input(file):
    return list(map(str.strip, open(file, "r+").readlines()))


def value_at(x, position):
    i, j = position
    if i < 0 or i >= len(x) or j < 0 or j >= len(x[0]):
        return
    return x[i][j]


def connections(x, position, coordinates):
    movement = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    new = [
        tuple(itertools.starmap(operator.add, zip(position, move))) for move in movement
    ]
    return [n if value_at(x, n) == value_at(x, position) else None for n in new]


def piece1(x, position, coordinates, area=0, perimeter=0):
    right, left, up, down = connections(x, position, coordinates)
    if position not in coordinates:
        return area, perimeter
    coordinates.pop(coordinates.index(position))
    area += 1
    if right:
        area, perimeter = piece1(x, right, coordinates, area, perimeter)
    if left:
        area, perimeter = piece1(x, left, coordinates, area, perimeter)
    if up:
        area, perimeter = piece1(x, up, coordinates, area, perimeter)
    if down:
        area, perimeter = piece1(x, down, coordinates, area, perimeter)
    return area, perimeter + 4 - sum(
        map(lambda x: 1 if x else 0, [right, left, up, down])
    )


coordinates = [(i, j) for i in range(len(x)) for j in range(len(x[0]))]
seen = []

direction = itertools.cycle(["right", "down", "left", "up"])


def piece2(x, starting, position, direction, side=0):
    right, *_ = connections(x, position, coordinates)
    if right == starting:
        return side
    if not right:
        side += 1
        i, j = position
        print(position)
        if next(direction) in ["down", "up"]:
            return piece2(rotate(x), starting, (9 - j, i), direction, side)
        return piece2(list(reversed(x)), starting, (i, j), direction, side)
    return piece2(x, starting, right, direction, side)


def rotate(x):
    return list(map(lambda x: "".join(x), map(reversed, x)))


piece2(x, (0, 0), (0, 0), direction)
piece2(x, (9, 9), coordinates)
piece2(x, (0, 4), coordinates)


# RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE
#


def part1(x):
    """
    >>> x = '''
    ... RRRRIICCFF
    ... RRRRIICCCF
    ... VVRRRCCFFF
    ... VVRCCCJFFF
    ... VVVVCJJCFE
    ... VVIVCCJJEE
    ... VVIIICJJEE
    ... MIIIIIJJEE
    ... MIIISIJEEE
    ... MMMISSJEEE
    ... '''.strip().splitlines()
    """
    price = 0
    coordinates = [(i, j) for i in range(len(x)) for j in range(len(x[0]))]
    while coordinates:
        position = coordinates[0]
        price += operator.mul(*piece1(x, position, coordinates))
    return price


def part2(x):
    price = 0
    coordinates = [(i, j) for i in range(len(x)) for j in range(len(x[0]))]
    while coordinates:
        position = coordinates[0]
        print(piece2(x, position, "right", coordinates))
    return price


if __name__ == "__main__":
    x = puzzle_input("inputs/12.txt")
    print("Part 1:", part1(x))
    print("Part 2:", part2(x))
