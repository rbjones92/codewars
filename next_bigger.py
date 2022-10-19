# Robert Jones
# 8/17.22
# Codewars - Next Bigger Number
# https://www.codewars.com/kata/55983863da40caa2c900004e/train/python


def next_bigger(n):

    num_list = [int(x) for x in str(n)]

    print(num_list)

    # If number is 1 digit
    if len(num_list) == 1:
        return -1

    # For 2 digit numbers
    if len(num_list) == 2:
        if num_list[0] < num_list[1]:
            return int(''.join(map(str,reversed(num_list))))
        else:
            return -1
        
    rev = []
    rev_2 = []

    for x in reversed(num_list):
        rev.append(x)

    swap_ind = []
    for x in range(0,len(rev)-1,1):
        if rev[x] > rev[x+1]:
            temp_1 = rev[x]
            temp_2 = rev[x+1]
            rev[x] = temp_2
            rev[x+1] = temp_1
            swap_ind = x
            break

    for i in reversed(rev):
        rev_2.append(i)

    print(rev_2)
    print(swap_ind)

    begin = rev_2[:swap_ind]
    end = sorted(rev_2[swap_ind::])

    result = begin+end

    result = int(''.join(map(str,rev_2)))
    
    if result == n:
        return -1
        
    print(result)
    return(result)

'''
next_bigger(21)
print('21',next_bigger(21))

next_bigger(3214)
print(next_bigger(3214))

next_bigger(35433566)
print(next_bigger(35433566))

next_bigger(1234567980)
print(next_bigger(1234567980))

next_bigger(531)
print(next_bigger(531))

next_bigger(111)
print(next_bigger(111))

next_bigger(1)
print(next_bigger(1))

next_bigger(24)
print(next_bigger(24))

'''

next_bigger(4991)

