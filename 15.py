from utils import neighbors4, parse_field
from heapq import heappush, heappop
import numpy as np


def solve(field: np.array):
    h, w = field.shape
    dp = np.zeros_like(field)
    heap = []
    used = set([(0, 0)])
    heappush(heap, (0, 0, 0))
    while heap:
        dist, i, j = heappop(heap)
        for ni, nj in neighbors4(i, j, h, w):
            if (ni, nj) not in used:
                dp[ni][nj] = dist + field[ni][nj]
                used.add((ni, nj))
                heappush(heap, (dp[ni][nj], ni, nj))
    return dp[-1][-1]


def part1(input):
    field = np.array(parse_field(input, int))
    return solve(field)


def part2(input):
    field = np.array(parse_field(input, int))
    h, w = field.shape
    new_field = np.vstack((np.hstack((field,) * 5),) * 5)
    new_field += np.arange(w * 5) // w
    new_field += (np.arange(h * 5) // h).reshape(-1, 1)
    new_field -= (new_field > 9) * 9
    return solve(new_field)
