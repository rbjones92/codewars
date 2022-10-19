# Robert Jones
# 8.19.22
# CodeWars - Sum Two Smallest Number


test = [19, 5, 42, 2, 77]


def sum_two_smallest_numbers(number):
    number = sorted(number)
    return number[0]+number[1]
