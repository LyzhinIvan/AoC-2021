from collections import deque
from math import prod

from utils import neighbors4


def low_points(lines):
    h, w = len(lines), len(lines[0])
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if all(c < lines[ni][nj] for ni, nj in neighbors4(i, j, h, w)):
                yield (i, j)


def part1(input):
    lines = input.strip().split('\n')
    return sum(int(lines[i][j]) + 1 for i, j in low_points(lines))


def calc_basin_size(li, lj, lines):
    h, w = len(lines), len(lines[0])
    dq = deque([(li, lj)])
    used = set([(li, lj)])
    while dq:
        i, j = dq.popleft()
        for ni, nj in neighbors4(i, j, h, w):
            p = (ni, nj)
            if p not in used and lines[ni][nj] != '9':
                used.add(p)
                dq.append(p)
    return len(used)


def part2(input):
    lines = input.strip().split('\n')
    sizes = sorted(calc_basin_size(li, lj, lines) for li, lj in low_points(lines))
    return prod(sizes[-3:])
