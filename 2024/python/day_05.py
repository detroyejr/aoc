"""Day 5"""


def split_line_by(x, split):
    return list(map(str.split, x.splitlines(), [split] * len(x)))


def puzzle_input(file):
    with open(file, "r+") as file:
        rules, update = file.read().split("\n\n")
        rules = split_line_by(rules, "|")
        update = split_line_by(update, ",")
        return rules, update


def follows_rules(update, rules):
    for low, high in rules:
        update_includes_numbers = low in update and high in update
        if update_includes_numbers and update.index(low) > update.index(high):
            return False
    return True


def sort_update(update, rules):
    while not follows_rules(update, rules):
        for low, high in rules:
            if (
                low in update
                and high in update
                and not update.index(low) < update.index(high)
            ):
                update[update.index(low)], update[update.index(high)] = (
                    high,
                    low,
                )
    return update


def part1(rules, updates):
    """
    >>> rules = [
    ...     ['47', '53'], ['97', '13'], ['97', '61'], ['97', '47'],
    ...     ['75', '29'], ['61', '13'], ['75', '53'], ['29', '13'],
    ...     ['97', '29'], ['53', '29'], ['61', '53'], ['97', '53'],
    ...     ['61', '29'], ['47', '13'], ['75', '47'], ['97', '75'],
    ...     ['47', '61'], ['75', '61'], ['47', '29'], ['75', '13'],
    ...     ['53', '13']
    ... ]
    >>> updates = [
    ...     ['75', '47', '61', '53', '29'],
    ...     ['97', '61', '53', '29', '13'],
    ...     ['75', '29', '13'],
    ...     ['75', '97', '47', '61', '53'],
    ...     ['61', '13' , '29'],
    ...     ['97', '13', '75', '29', '47']
    ... ]
    >>> part1(rules, updates)
    143
    """
    valid_updates = [update for update in updates if follows_rules(update, rules)]
    return sum(map(lambda x: int(x[int(len(x) / 2)]), valid_updates))


def part2(rules, updates):
    """
    >>> rules = [
    ...     ['47', '53'], ['97', '13'], ['97', '61'], ['97', '47'],
    ...     ['75', '29'], ['61', '13'], ['75', '53'], ['29', '13'],
    ...     ['97', '29'], ['53', '29'], ['61', '53'], ['97', '53'],
    ...     ['61', '29'], ['47', '13'], ['75', '47'], ['97', '75'],
    ...     ['47', '61'], ['75', '61'], ['47', '29'], ['75', '13'],
    ...     ['53', '13']
    ... ]
    >>> updates = [
    ...     ['75', '47', '61', '53', '29'],
    ...     ['97', '61', '53', '29', '13'],
    ...     ['75', '29', '13'],
    ...     ['75', '97', '47', '61', '53'],
    ...     ['61', '13' , '29'],
    ...     ['97', '13', '75', '29', '47']
    ... ]
    >>> part2(rules, updates)
    123
    """
    invalid_updates = [update for update in updates if not follows_rules(update, rules)]

    results = []
    for u in invalid_updates:
        results.append(sort_update(u, rules.copy()))
    return sum(map(lambda x: int(x[int(len(x) / 2)]), results))


if __name__ == "__main__":
    rules, updates = puzzle_input("inputs/05.txt")
    print("Part 1:", part1(rules, updates))
    print("Part 2:", part2(rules, updates))
