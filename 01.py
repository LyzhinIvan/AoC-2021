import numpy as np


def part1(input):
    '''
    Count the number of times a measurement increases from the previous measurement.
    '''
    numbers = np.array(list(map(int, input.split())))
    return (numbers[:-1] < numbers[1:]).sum()


def part2(input):
    '''
    Count the number of times a sum of measurements in 3-width sliding window
    increases from the previous sum of measurements in 3-width sliding window.
    '''
    numbers = np.array(list(map(int, input.split())))
    return (numbers[:-3] < numbers[3:]).sum()
