def parse_command(line):
    cmd, delta = line.split()
    return cmd, int(delta)


def parse_commands(input):
    return map(parse_command, input.strip().split('\n'))


def part1(input):
    '''
    Multiply final depth and position if:
    * down X - increase depth by X
    * up X - decrease depth by X
    * forward X - increase position by X
    '''
    pos, depth = 0, 0
    for cmd, delta in parse_commands(input):
        if cmd == 'down':
            depth += delta
        if cmd == 'up':
            depth -= delta
        elif cmd == 'forward':
            pos += delta
    return pos * depth


def part2(input):
    '''
    Multiply final depth and position if:
    * down X - increase aim by X
    * up X - decrease aim by X
    * forward X - increase position by X and depth by X*aim
    '''
    pos, depth, aim = 0, 0, 0
    for cmd, delta in parse_commands(input):
        if cmd == 'down':
            aim += delta
        elif cmd == 'up':
            aim -= delta
        elif cmd == 'forward':
            depth += aim * delta
            pos += delta
    return pos * depth
