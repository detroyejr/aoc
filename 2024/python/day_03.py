"""Day 3"""

import re

INSTRUCTION = re.compile(r"mul\(\d{1,3},\d{1,3}\)")

# NOTE: The pattern "do\(\).*?don\'t\(\)" won't match instructions that contain
# line terminators so the count was short.
# (?s:.*?) allows for matches that include new lines.
DO_INSTRUCTION = re.compile(r"^(?s:.*?)don't\(\)|do\(\)(?s:.*?)don\'t\(\)")


def puzzle_input(file):
    with open(file, "r+") as file:
        return file.read()


def mul(x, y):
    return x * y


# Original non regex solution to part 2.
def valid_instructions(x):
    return list(map(lambda x: x.split("don't()")[0], x.split("do()")))


def part1(x):
    """
    >>> part1((
    ...     "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+"
    ...     "mul(32,64]then(mul(11,8)mul(8,5))"
    ... ))
    161
    """
    return sum(map(eval, INSTRUCTION.findall(x)))


def part2(x):
    """
    >>> part2((
    ...     "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+"
    ...     "mul(32,64](mul(11,8)undo()?mul(8,5))"
    ... ))
    48
    """
    return sum(map(part1, DO_INSTRUCTION.findall(x)))


if __name__ == "__main__":
    x = puzzle_input("inputs/03.txt")
    print("Part 1:", part1(x))
    print("Part 2:", part2(x))
