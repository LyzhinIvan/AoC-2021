import numpy as np


def to_int(x):
    return int(''.join((map(str, map(int, x)))), base=2)


def part1(input):
    '''
    Multiply gamma and espilon rate.
    Details: https://adventofcode.com/2021/day/3
    '''
    lines = input.strip().split('\n')
    report = np.array([list(map(int, line)) for line in lines])
    gamma = report.sum(axis=0) > len(lines) / 2
    eps = ~gamma
    return to_int(gamma) * to_int(eps)


def select(report, predicate):
    for bit in range(report.shape[1]):
        part = predicate(int(report[:, bit].sum()) * 2, len(report))
        report = report[report[:, bit] == part]
        if len(report) == 1:
            break
    assert len(report) == 1
    return report[0]


def part2(input):
    '''
    Multiply oxy and co2 rate.
    Details: https://adventofcode.com/2021/day/3
    '''
    lines = input.strip().split('\n')
    report = np.array([list(map(int, line)) for line in lines], dtype=int)
    oxy = select(report, int.__ge__)
    co2 = select(report, int.__lt__)
    return to_int(oxy) * to_int(co2)
