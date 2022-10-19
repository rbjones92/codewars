# Robert Jones
# 8.24.22
# CodeWars - Sum of Pairs - https://www.codewars.com/kata/54d81488b981293527000c8f/train/python


# My solution... too slow
def sum_pairs(ints, s):

    pair = []

    for i in range(len(ints)):
        for j in range(i+1,len(ints)):
            if ints[i]+ints[j] == s:
                pair.append([ints[i],ints[j],j])
                if len(pair) == 2:
                    return sorted(pair,key = lambda x : x[2])[0][:2]
    
    if len(pair) == 1:
        return pair[0][:2]

    if pair == []:
        return None


print(sum_pairs([1, 4, 8, 7, 3, 15,1, -2, 3, 0, -6, 1,1, -2, 3, 0, -6, 1,1, -2, 3, 0, -6, 1,1, -2, 3, 0, -6, 1],8))

