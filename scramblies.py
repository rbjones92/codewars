# Robert Jones
# 8.24.22
# CodeWars - Scramblies - https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python


def scramble(s1, s2):

    for i in s2:
        if i in s1:
            s1 = s1.replace(i,'')    
        else:
            return False

    else:
        return True


print(scramble('scriptjava', 'javascript'))


