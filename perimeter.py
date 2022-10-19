# Robert Jones
# 8.24.22
# CodeWars - perimeter - https://www.codewars.com/kata/559a28007caad2ac4e000083/train/python



fib = [1,1,2]

def perimeter(n):

    for i in range(0,n,1):
        next = fib[-1] + fib[-2]
        fib.append(next)
        if len(fib) == n+1:
            return sum(fib)*4


print(perimeter(7))