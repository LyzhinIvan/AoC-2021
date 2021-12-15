from typing import Iterator
import re


def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def flatten(list2):
    return [x for sublist in list2 for x in sublist]


def transpose(list2):
    return list(zip(*list2))


def last(iterable):
    *_, last_item = iterable
    return last_item


def parse_blocks(input, sep=None):
    blocks = []
    block = []
    for line in input.strip().split('\n'):
        if line:
            block.append(parse_line(line, sep=sep))
        elif block:
            blocks.append(block)
            block = []
    if block:
        blocks.append(block)
    return blocks


def parse_line(line, sep=None):
    parts = line.split() if sep is None else re.split(sep, line)
    return [parse_value(item) for item in parts if item != '']


def parse_value(value):
    i = try_parse_int(value)
    if i is not None:
        return i
    f = try_parse_float(value)
    if f is not None:
        return f
    return value


def try_parse_int(value):
    try:
        return int(value)
    except ValueError:
        return None


def try_parse_float(value):
    try:
        return float(value)
    except ValueError:
        return None


def neighbors4(i, j, h, w):
    for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        if 0 <= i + di < h and 0 <= j + dj < w:
            yield (i + di, j + dj)


def neighbors8(i, j, h, w):
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if (di != 0 or dj != 0) and 0 <= i + di < h and 0 <= j + dj < w:
                yield (i + di, j + dj)


def inv_dict(d: dict) -> dict:
    return dict((value, key) for key, value in d.items())


def minmax(iterable):
    if not isinstance(iterable, Iterator):
        iterable = iter(iterable)
    mn = mx = next(iterable)
    for value in iterable:
        mn = min(mn, value)
        mx = max(mx, value)
    return mn, mx


def parse_field(input, type):
    return list(map(lambda line: list(map(type, list(line))), input.strip().split('\n')))
