"""
Backend for Average Calculator
by PatrickSoup

"""


# Get mean of numbers
def mean(numbers):
    # Mean: Divide total by count
    answer = 0
    for i in numbers:
        answer += i         # add all numbers
    answer /= len(numbers)  # divide by count
    return answer


# Get mode of numbers
def mode(numbers):
    # Mode: Most common number
    answer = 0

    return answer


def _test():
    # set numbers
    numbers = [2, 99, 32, 0.4, 32]
    # calculate
    _mode = mode(numbers)
    _mean = mean(numbers)
    _range = range_(numbers)
    _median = median(numbers)
    # convert to string
    _mode = str(_mode)
    _mean = str(_mean)
    _median = str(_median)
    _range = str(_range)
    # concatenate and print
    print('mean=', _mean, '\nmode=', _mode, '\nmedian=', _median, '\nrange=', _range)
