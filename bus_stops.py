# Robert Jones
# 8.19.22
# Codewars - https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python. Bus stops


test = [[10,0],[3,5],[5,8]]


def number(bus_stops):
    total = 0
    for i in bus_stops:
        total += i[0]-i[1]
    return total

print(number(test))

