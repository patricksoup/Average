"""
Backend for Average Calculator
by PatrickSoup
v 1.0
"""


from collections import Counter
import math


# get mean of numbers
def mean(numbers):
    # mean: divide total by count
    answer = 0
    for i in numbers:
        answer += i         # add all numbers
    answer /= len(numbers)  # divide by count
    return answer


# Get mode of numbers
def mode(numbers):
    # Mode: Most common number
    # TODO: Do it myself
    data = Counter(numbers)  # use collections.Counter to work out
    answer = data.most_common(1)  # returns the highest occurring item
    return answer[0][0]


def median(numbers):
    # Median: Middle number
    numbers = sorted(numbers)  # sort in order
    length = len(numbers)  # find length

    if length % 2 == 0:  # is even number
        index1 = length/2  # find first of 2 middles as if was 1-indexed, or, 2nd as 0-indexed (as is)
        index2 = index1-1  # find second middle (0-indexed)
        value1 = numbers[index1]  # find value with index
        value2 = numbers[index2]  # ditto ^
        answer = mean([value1, value2])  # get mean because even number

        return answer
    else:  # is odd number
        index = length/2
        index = math.ceil(index)  # find middle as if was 1-indexed
        index -= 1  # turn into 0-indexed value

        return numbers[index]


def range_(numbers):
    # difference between highest and lowest in list
    small = min(numbers)  # find smallest
    large = max(numbers)  # find largest
    answer = large - small  # find difference
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

if __name__ == "__main__":
    _test()