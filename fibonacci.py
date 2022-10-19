# Robert Jones
# 8.24.22
# CodeWars - fib_numsi - https://www.codewars.com/kata/529adbf7533b761c560004e5/train/python

import sys

sys.setrecursionlimit(1500)


memo = {}

def perimeter(n):


    memo = {}

    def fibonacci(n):
        if n in [0, 1]:
            return n
        if n not in memo:
            memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
        
        return memo[n]


    fibonacci(n+1)
    memo["1"] = 1 

    s = sum(memo.values())
    return s * 4

print(perimeter(1000))
