from collections import defaultdict
from typing import Callable, Dict, List

from utils import parse_blocks


Graph = Dict[str, List[str]]
UsedDict = Dict[str, int]
CanMovePredicate = Callable[[str, UsedDict], bool]


def can_move_1(v: str, used: UsedDict, was_twice_step: bool) -> bool:
    return v.isupper() or not used[v]


def can_move_2(v: str, used: UsedDict, was_twice_step: bool) -> bool:
    return v != 'start' and (v.isupper() or not used[v] or not was_twice_step)


def dfs(u: str, graph: Graph, used: UsedDict, can_move: CanMovePredicate, was_twice_step: bool = False) -> int:
    if u == 'end':
        return 1

    if u.islower():
        used[u] += 1
    was_twice_step |= (used[u] > 1)

    result = 0
    for v in graph[u]:
        if can_move(v, used, was_twice_step):
            result += dfs(v, graph, used, can_move, was_twice_step)

    if u.islower():
        used[u] -= 1

    return result


def parse_graph(block) -> Graph:
    graph = defaultdict(list)
    for line in block:
        u, v = line[0].split('-')
        graph[u].append(v)
        graph[v].append(u)
    return graph


def solve(input, can_move: CanMovePredicate) -> int:
    for block in parse_blocks(input):
        graph = parse_graph(block)
        used = defaultdict(int)
        result = dfs('start', graph, used, can_move)
        print(result)
    return result


def part1(input):
    return solve(input, can_move_1)


def part2(input):
    return solve(input, can_move_2)
