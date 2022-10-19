# Robert Jones
# 8.19.22
# Codewards - Valid Braces - https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python



def valid_braces(string):

    opened = ['(','{','[']
    closed = [')','}',']']

    if len(string) % 2 == 1:
        return False

    rev = []

    if type(string) == str:
        string = list(str(string))
        for i in range(len(string)-1,-1,-1):
            rev.append(string[i])

    else:
        for i in reversed(string):
            rev.append(i)


    for i in range(0,len(string),1):

        if string[0] in closed:
            return False

        for q in range(0,len(opened),1):
            if string[i] == opened[q] and rev[i] == closed[q]:
                string[i] = ''
                string[-i-1] = ''
    
    for i in string:
        if i != '':
            return False

    else:
        print(string)
        return True


    
    



print(valid_braces('{}()[]'))
