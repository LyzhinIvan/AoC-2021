from utils import parse_blocks


def part1(input):
    cnt = 0
    for line in parse_blocks(input)[0]:
        cnt += sum(1 for part in line[-4:] if len(part) in (2, 3, 4, 7))
    return cnt


def part2(input):
    s = 0
    for line in parse_blocks(input)[0]:
        left, right = line[:10], line[-4:]
        left = list(map(frozenset, left))
        right = list(map(frozenset, right))

        mapping = {}
        mapping[8] = next(x for x in left if len(x) == 7)
        mapping[7] = next(x for x in left if len(x) == 3)
        mapping[1] = next(x for x in left if len(x) == 2)
        mapping[4] = next(x for x in left if len(x) == 4)
        mapping[9] = next(x for x in left if len(x) == 6 and len(x - mapping[4] - mapping[7]) == 1)
        mapping[6] = next(x for x in left if len(x) == 6 and x != mapping[9] and len(x - mapping[1]) == 5)
        mapping[0] = next(x for x in left if len(x) == 6 and x != mapping[9] and len(x - mapping[1]) == 4)
        mapping[2] = next(x for x in left if len(x) == 5 and len(x - mapping[4]) == 3)
        mapping[3] = next(x for x in left if len(x) == 5 and x != mapping[2] and len(x - mapping[1]) == 3)
        mapping[5] = next(x for x in left if len(x) == 5 and x != mapping[2] and len(x - mapping[1]) == 4)

        inv_mapping = dict((value, key) for key, value in mapping.items())
        s += int(''.join(map(str, (inv_mapping[part] for part in right))))

    return s
