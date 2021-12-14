from utils import minmax, parse_blocks
from collections import Counter


def solve(input, steps):
    blocks = parse_blocks(input)
    template = blocks[0][0][0]
    rules = dict((line[0], line[2]) for line in blocks[1])
    template = '_' + template + '_'
    cntr = Counter(x+y for x, y in zip(template, template[1:]))
    for _ in range(steps):
        new_cntr = cntr.copy()
        for (left, right), middle in rules.items():
            value = cntr[left + right]
            new_cntr[left + right] -= value
            new_cntr[left + middle] += value
            new_cntr[middle + right] += value
        cntr = new_cntr
    letter_cntr = Counter()
    for (left, right), value in cntr.items():
        letter_cntr[right] += value
    letter_cntr.pop('_')
    mn, mx = minmax(letter_cntr.values())
    return mx - mn


def part1(input):
    return solve(input, steps=10)


def part2(input):
    return solve(input, steps=40)
