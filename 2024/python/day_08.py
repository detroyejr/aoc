"""Day 8"""

import itertools
import operator


def puzzle_input(file):
    with open(file, "r+") as file:
        x = list(map(str.strip, file.readlines()))
        return x


def nodes(x, char):
    return [(i, j) for i in range(len(x)) for j in range(len(x[i])) if x[i][j] == char]


def distance(coords):
    return tuple(itertools.starmap(operator.sub, zip(*reversed(coords))))


def piece1(coords, dist):
    sub, add = zip(coords, [dist] * 2)
    return tuple(itertools.starmap(operator.sub, zip(*sub))), tuple(
        itertools.starmap(operator.add, zip(*add))
    )


def piece2(x, dist, coords):
    left, right = piece1(coords, dist)
    result = [coords, (left, right)]
    while valid_antinode(x, left) or valid_antinode(x, right):
        left, right = piece1((left, right), dist)
        result.append((left, right))
    return [node for node in result for node in node if valid_antinode(x, node)]


def valid_antinode(x, node):
    i, j = node
    return 0 <= i < len(x) and 0 <= j < len(x[0])


def part1(x):
    """
    >>> x = '''
    ...    ............
    ...    ........0...
    ...    .....0......
    ...    .......0....
    ...    ....0.......
    ...    ......A.....
    ...    ............
    ...    ............
    ...    ........A...
    ...    .........A..
    ...    ............
    ...    ............
    ... '''.strip().splitlines()
    >>> x = list(map(str.strip, x))
    >>> part1(x)
    14
    """
    connections = [
        itertools.combinations(nodes(x, char), 2)
        for char in set(itertools.chain(*x)).difference(".")
    ]
    return len(
        {
            c
            for connection in connections
            for c in connection
            for c in piece1(c, distance(c))
            if valid_antinode(x, c)
        }
    )


def part2(x):
    """
    >>> x = '''
    ...    ............
    ...    ........0...
    ...    .....0......
    ...    .......0....
    ...    ....0.......
    ...    ......A.....
    ...    ............
    ...    ............
    ...    ........A...
    ...    .........A..
    ...    ............
    ...    ............
    ... '''.strip().splitlines()
    >>> x = list(map(str.strip, x))
    >>> part2(x)
    34
    """
    connections = [
        itertools.combinations(nodes(x, char), 2)
        for char in set(itertools.chain(*x)).difference(".")
    ]
    return len(
        {
            c
            for connection in connections
            for c in connection
            for c in piece2(x, distance(c), c)
        }
    )


if __name__ == "__main__":
    x = puzzle_input("inputs/08.txt")
    print("Part 1:", part1(x))
    print("Part 2:", part2(x))
