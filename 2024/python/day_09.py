"""Day 9"""

import copy
import itertools
import operator


def puzzle_input(file):
    return open(file, "r+").read().strip()


def piece1(x):
    x = list(itertools.chain(*x))
    i, j = 0, len(x) - 1
    while i < j:
        if x[i] != ".":
            i += 1
            continue
        if x[j] == ".":
            j -= 1
            continue
        x[i], x[j] = x[j], x[i]
        i += 1
        j -= 1
    return x


def piece2(x):
    result = copy.deepcopy(x)
    while x:
        move = x.pop()
        move = move[: len(move) if "." not in move else move.index(".")]
        for element in result[: len(x)]:
            if "." in element and element.count(".") >= len(move):
                start = element.index(".")
                end = start + len(move)
                element[start:end] = move
                result[len(x)][: len(move)] = ["."] * len(move)
                break
    return result


def parse_block(block_id, x):
    if len(x) == 1:
        (block,) = x
        return [str(block_id)] * int(block)
    block, free_space = x
    return [str(block_id)] * int(block) + ["."] * int(free_space)


def part1(x):
    """
    >>> part1('2333133121414131402')
    1928
    """
    x = enumerate(itertools.batched(x, 2))
    x = [parse_block(block_id, x) for block_id, x in x]
    x = piece1(x)
    x = enumerate([int(x) for x in x if x != "."])
    return sum(itertools.starmap(operator.mul, x))


def part2(x):
    """
    >>> part2('2333133121414131402')
    2858
    """
    x = enumerate(itertools.batched(x, 2))
    x = [parse_block(block_id, x) for block_id, x in x]
    x = piece2(x)
    x = list(itertools.chain(*x))
    return sum(
        itertools.starmap(
            operator.mul, [(i, int(x)) for i, x in enumerate(x) if "." not in x]
        )
    )


if __name__ == "__main__":
    x = puzzle_input("inputs/09.txt")
    print("Part 1:", part1(x))
    print("Part 2:", part2(x))
