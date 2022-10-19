# Robert Jones
# 8.24.22
# CodeWars - Sum of Pairs - https://www.codewars.com/kata/54d81488b981293527000c8f/train/python


# CodeWars Clever Solution 

def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)


print(sum_pairs([1, 4, 8, 7, 3, 15,1, -2, 3, 0, -6, 1,1, -2, 3, 0, -6, 1,1, -2, 3, 0, -6, 1,1, -2, 3, 0, -6, 1],8))
