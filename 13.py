from utils import parse_blocks


def apply_fold(dots, fold):
    axis, pos = fold
    if axis == 'x':
        return set((pos - abs(x - pos), y) for x, y in dots)
    else:
        return set((x, pos - abs(y - pos)) for x, y in dots)


def parse_input(input):
    blocks = parse_blocks(input, sep='\s|,|=')
    dots = set(map(tuple, blocks[0]))
    folds = [(axis, pos) for _, _, axis, pos in blocks[1]]
    return dots, folds


def part1(input):
    dots, folds = parse_input(input)
    dots = apply_fold(dots, folds[0])
    return len(dots)


def part2(input):
    dots, folds = parse_input(input)
    for fold in folds:
        dots = apply_fold(dots, fold)

    field = [[' '] * 40 for _ in range(6)]
    for x, y in dots:
        field[y][x] = '█'
    print('\n'.join(''.join(line) for line in field))
