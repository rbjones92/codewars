# Robert Jones
# 8.30.22
# CodeWars - The observed PIN - https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python

pin = '369'

from itertools import product

def get_pins(observed):

    pin_map = {0:[0,8],1:[1,2,4],2:[2,1,3,5],3:[3,2,6],4:[4,1,7,5],5:[5,2,4,6,8],6:[6,3,5,9],7:[7,4,8],8:[8,5,7,9,0],9:[9,6,8]}

    possible = []
    
    for j in observed:
        for i in pin_map.items():
            if str(i[0]) == j:
                possible.append(i[1])

    res = list(product(*possible))
    
    res = [list(ele) for ele in res]

    for i in range(0,len(res)):
        res[i] = str(res[i]).replace(',','')
        res[i] = str(res[i]).replace(' ','')
        res[i] = str(res[i]).replace('[','')
        res[i] = str(res[i]).replace(']','')

    return res


print(get_pins(pin))
