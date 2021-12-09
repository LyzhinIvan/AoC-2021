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
