"""Day 1"""


def puzzle_input(file):
    with open(file, "r+") as file:
        return zip(*[r.strip().split("   ") for r in file.readlines()])


def part1(x, y):
    """
    >>> x = [3, 4, 2, 1, 3, 3]
    >>> y = [4, 3, 5, 3, 9, 3]
    >>> part1(x, y)
    11
    """
    return sum(map(lambda i, j: abs(int(j) - int(i)), sorted(x), sorted(y)))


def part2(x, y):
    """
    >>> x = [3, 4, 2, 1, 3, 3]
    >>> y = [4, 3, 5, 3, 9, 3]
    >>> part2(x, y)
    31
    """
    return sum(map(lambda i: abs(int(i) * y.count(i)), x))


if __name__ == "__main__":
    x, y = puzzle_input("inputs/01.txt")
    print("Part 1:", part1(x, y))
    print("Part 2:", part2(x, y))
