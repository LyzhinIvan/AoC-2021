from collections import defaultdict
from utils import parse_blocks, sign


def segments(input):
    return (segment for segment in parse_blocks(input, sep=',| -> ')[0])


def is_vert_or_hor(segment):
    x1, y1, x2, y2 = segment
    return x1 == x2 or y1 == y2


def solve(segments):
    d = defaultdict(int)
    for x1, y1, x2, y2 in segments:
        sx = sign(x2 - x1)
        sy = sign(y2 - y1)
        steps = max(abs(x2 - x1), abs(y2 - y1)) + 1
        for step in range(steps):
            x = x1 + step * sx
            y = y1 + step * sy
            d[(x, y)] +=  1
    cnt = sum(1 for value in d.values() if value > 1)
    return cnt


def part1(input):
    return solve(filter(is_vert_or_hor, segments(input)))


def part2(input):
    return solve(segments(input))
