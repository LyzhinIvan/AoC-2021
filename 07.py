import numpy as np

from utils import parse_line


def part1(input):
    xs = np.array(parse_line(input, sep=','))
    pos = int(np.median(xs))
    return np.abs(xs - pos).sum()


def part2(input):
    xs = np.array(parse_line(input, sep=','))
    def cost(pos):
        return (np.square(xs - pos) + np.abs(xs - pos)).sum() // 2
    best = np.mean(xs)
    return min(cost(int(best)), cost(int(best) + 1))
