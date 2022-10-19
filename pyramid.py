# Robert Jones
# 8.30.22
# CodeWars - Pyramid Slide Down - https://www.codewars.com/kata/551f23362ff852e2ab000037/train/python

# solution online
def longest_slide_down(pyramid):
    l = len(pyramid)
    for i in range(l-2,-1,-1):
        for j in range(i+1):
            x = max([pyramid[i+1][j],pyramid[i+1][j+1]])+pyramid[i][j]
            pyramid[i][j] = x
            print(pyramid)
    print(pyramid[0][0])
    return pyramid[0][0]


longest_slide_down([
            [10],
            [95, 5],
            [130, 47, 222],
            [152, 35, 87, 1],
            [150,  4, 40, 20, 300],
            ])