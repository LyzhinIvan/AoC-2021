from utils import flatten, last, parse_blocks


def winners(input):
    numbers, *boards = parse_blocks(input)
    numbers = list(map(int, numbers[0][0].split(',')))
    completed_boards = set()
    for draw_value in numbers:
        for board_id, board in enumerate(boards):
            if board_id in completed_boards:
                continue
            for r, row in enumerate(board):
                for c, board_value in enumerate(row):
                    if board_value == draw_value:
                        board[r][c] = None
                        is_completed = all(board[r][i] is None for i in range(5))
                        is_completed |= all(board[i][c] is None for i in range(5))
                        if is_completed:
                            completed_boards.add(board_id)
                            yield sum(filter(None, flatten(board))) * draw_value


def part1(input):
    return next(winners(input))


def part2(input):
    return last(winners(input))
