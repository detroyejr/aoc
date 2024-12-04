"""Day 4"""

import itertools


def puzzle_input(file):
    with open(file, "r+") as file:
        return list(map(str.strip, file.readlines()))


def piece1(x, position, move):
    index = [tuple(map(sum, zip(position, m))) for m in move]
    if not all([0 <= i < len(x) for index in index for i in index]):
        return ""
    return "".join(itertools.starmap(lambda i, j: x[i][j], index))


def piece2(x, position, movement):
    options = ["MAS", "SAM"]
    p1 = map(lambda m: piece1(x, position, m), movement)
    return all(map(lambda o: o in options, p1))


def part1(x):
    """
    >>> x = [
    ...     "MMMSXXMASM",
    ...     "MSAMXMSMSA",
    ...     "AMXSXMAAMM",
    ...     "MSAMASMSMX",
    ...     "XMASAMXAMM",
    ...     "XXAMMXXAMA",
    ...     "SMSMSASXSS",
    ...     "SAXAMASAAA",
    ...     "MAMMMXMMMM",
    ...     "MXMXAXMASX",
    ... ]
    >>> part1(x)
    18
    """
    coordinates = [(i, j) for i in range(len(x)) for j in range(len(x))]
    movement = [
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (0, -1), (0, -2), (0, -3)],
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(0, 0), (-1, 0), (-2, 0), (-3, 0)],
        [(0, 0), (1, 1), (2, 2), (3, 3)],
        [(0, 0), (-1, -1), (-2, -2), (-3, -3)],
        [(0, 0), (1, -1), (2, -2), (3, -3)],
        [(0, 0), (-1, 1), (-2, 2), (-3, 3)],
    ]

    return sum(
        [
            1 if piece1(x, position, move) == "XMAS" else 0
            for position in coordinates
            for move in movement
        ]
    )


def part2(x):
    """
    >>> x = [
    ...     "MMMSXXMASM",
    ...     "MSAMXMSMSA",
    ...     "AMXSXMAAMM",
    ...     "MSAMASMSMX",
    ...     "XMASAMXAMM",
    ...     "XXAMMXXAMA",
    ...     "SMSMSASXSS",
    ...     "SAXAMASAAA",
    ...     "MAMMMXMMMM",
    ...     "MXMXAXMASX",
    ... ]
    >>> part2(x)
    9
    """
    coordinates = [(i, j) for i in range(len(x)) for j in range(len(x))]
    movement = [
        [(-1, -1), (0, 0), (1, 1)],
        [(-1, 1), (0, 0), (1, -1)],
    ]

    return sum([1 if piece2(x, position, movement) else 0 for position in coordinates])


if __name__ == "__main__":
    x = puzzle_input("inputs/04.txt")
    print("Part 1:", part1(x))
    print("Part 2:", part2(x))
