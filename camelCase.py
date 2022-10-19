# Robert Jones
# 8.19.22
# Codewars - Break camelCase - https://www.codewars.com/kata/5208f99aee097e6552000148/train/python



test = 'breakCamelCase'


def solution(s):
    ind = []
    for i in range(0,len(s),1):
        if s[i].isupper():
            ind.append(i)

    s = list(s)
    counter = 0
    for i in ind:
        s.insert(i+counter," ")
        counter = counter + 1
    
    s = ''.join(s)
    return s

print(solution(test))