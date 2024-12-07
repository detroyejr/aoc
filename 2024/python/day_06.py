"""Day 6"""

import itertools


def puzzle_input(file):
    with open(file, "r+") as file:
        x = file.read()
        x = x.replace(" ", "").replace("\n", "")
        return bytearray(x.encode())


def off_grid(x, position, facing, movement):
    n = int(len(x) ** 0.5)
    if facing == b"^" or facing == b"v":
        return (position + movement[facing]) < 0 or (position + movement[facing]) > len(
            x
        )
    elif facing == b">":
        return (position % n) > (position + movement[facing]) % n
    else:
        return (position % n) < (position + movement[facing]) % n


def part1(x):
    """
    >>> x = bytearray((
    ...     b'....#..............#.......'
    ...     b'.....#..............#......'
    ...     b'.......#..^.............#.#'
    ...     b'...............#...'
    ... ))
    >>> part1(x)
    41
    """
    direction = itertools.cycle([b"^", b">", b"v", b"<"])
    movement = {
        b"^": -int(len(x) ** 0.5),
        b">": 1,
        b"v": int(len(x) ** 0.5),
        b"<": -1,
    }
    facing = next(direction)
    while True:
        if facing not in x:
            facing = next(direction)
            continue
        position = x.index(facing)
        if off_grid(x, position, facing, movement):
            x[position] = 88
            break
        if x[position + movement[facing]] != 35:
            x[position], x[position + movement[facing]] = 88, facing[0]
            position += movement[facing]
        else:
            facing = next(direction)
            x[position] = facing[0]
    return x.count(b"X")


def chunk_string(string, n):
    """
    Splits a string into chunks of size n.

    Args:
        string (str): The input string to be chunked.
        n (int): The size of each chunk.

    Returns:
        list: A list of string chunks.
    """
    return [string[i : i + n] for i in range(0, len(string), n)]


def part2(x):
    """
    >>> x = bytearray((
    ...     b'....#..............#.......'
    ...     b'.....#..............#......'
    ...     b'.......#..^.............#.#'
    ...     b'...............#...'
    ... ))
    >>> part2(x)
    41
    """
    direction = itertools.cycle([b"^", b">", b"v", b"<"])
    right = itertools.cycle([b">", b"v", b"<", b"^"])
    movement = {
        b"^": -int(len(x) ** 0.5),
        b">": 1,
        b"v": int(len(x) ** 0.5),
        b"<": -1,
    }
    facing = next(direction)
    turn = next(right)
    new_obstacle = 0
    while True:
        if facing not in x:
            facing = next(direction)
            turn = next(right)
            continue
        position = x.index(facing)
        if off_grid(x, position, facing, movement):
            x[position] = 88
            break
        if x[position + movement[facing]] != 35:
            if x[position + movement[turn]] == 88:
                new_obstacle += 1
            x[position], x[position + movement[facing]] = 88, facing[0]
            position += movement[facing]
        else:
            facing = next(direction)
            turn = next(right)
            x[position] = facing[0]
    return new_obstacle


if __name__ == "__main__":
    x = puzzle_input("inputs/06.txt")
    print("Part 1:", part1(x))
    # FIXME:
    print("Part 2:", part2(x))
