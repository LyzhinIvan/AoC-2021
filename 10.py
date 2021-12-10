import numpy as np


OPEN_TO_CLOSE = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
OPENS = OPEN_TO_CLOSE.keys()


def part1(input):
    s = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    score = 0
    for line in input.strip().split('\n'):
        stack = []
        for c in line:
            if c in OPENS:
                stack.append(c)
            else:
                if not stack:
                    break
                elif OPEN_TO_CLOSE[stack[-1]] != c:
                    score += s[c]
                    break
                stack.pop()
    return score


def part2(input):
    s = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }
    scores = []
    for line in input.strip().split('\n'):
        stack = []
        for c in line:
            if c in OPENS:
                stack.append(c)
            else:
                if not stack or OPEN_TO_CLOSE[stack[-1]] != c:
                    break
                stack.pop()
        else:
            line_score = 0
            while stack:
                c = stack.pop()
                line_score = line_score * 5 + s[c]
            scores.append(line_score)

    return int(np.median(scores))
