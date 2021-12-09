from collections import defaultdict

from utils import parse_line


def simulate(input, days):
    numbers = parse_line(input, sep=',')
    state = defaultdict(int)
    for x in numbers:
        state[x] += 1
    for _ in range(days):
        next_state = defaultdict(int)
        for value, cnt in state.items():
            if value > 0:
                next_state[value - 1] += cnt
            else:
                next_state[6] += cnt
                next_state[8] += cnt
        state = next_state
    return sum(state.values())


def part1(input):
    '''
    How many lanternfishs will be after 80 days?
    '''
    return simulate(input, 80)


def part2(input):
    '''
    How many lanternfishs will be after 256 days?
    '''
    return simulate(input, 256)
