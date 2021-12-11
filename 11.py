from utils import *
from collections import deque


def simulate_step(field):
    h, w = len(field), len(field[0])
    flash_count = 0
    flash_queue = deque()

    for i in range(h):
        for j in range(w):
            field[i][j] += 1
            if field[i][j] == 10:
                flash_queue.append((i, j))

    while flash_queue:
        i, j = flash_queue.popleft()
        flash_count += 1
        for ni, nj in neighbors8(i, j, h, w):
            if field[ni][nj] > 9:
                continue
            field[ni][nj] += 1
            if field[ni][nj] == 10:
                flash_queue.append((ni, nj))

    for i in range(h):
        for j in range(w):
            if field[i][j] > 9:
                field[i][j] = 0

    return flash_count


def parse_field(input):
    return list(map(lambda line: list(map(int, list(line))), input.strip().split('\n')))


def part1(input):
    field = parse_field(input)
    return sum(simulate_step(field) for _ in range(100) )


def part2(input):
    field = parse_field(input)
    h, w = len(field), len(field[0])
    return next(step for step in range(1, 1000) if simulate_step(field) == h * w)
