# Robert Jones
# 9.6.22
# Codewars - nesting structure comparison - https://www.codewars.com/kata/520446778469526ec0000001/train/python

import re

def same_structure_as(original,other):

    if original == other:
        return True    

    s = re.sub('[?!0-9a-zA-Z]+', '*', str(original))
    s2 = re.sub('[?!0-9a-zA-Z]+', '*', str(other))

    s = s.replace('-','')
    s2 = s2.replace('-','')

    print(s)
    print(s2)
    
    if s == s2:
        return True
    
    else:
        return False
    


og = [19, -8, -1, [], 10, -4, 1, -11, 20, [14, -3, 11, 12], [5, -2, [[19, [14, [[], 11, 12, [-15, -16, 7, [-20, -6, [], 8]]]]], -12, -19, 17], -1], 2, 15, [], 6, -14, 19, 1, -12, -3, [-3, -9, [-10, 6, [[-1, -19], -7], 16], 10], -4, [20, 8], 20, -5, -13, 14, -13, 1, -13, 10, -5] 
ot = [-19, -9, -7, [], -5, 16, 19, -2, 8, [-18, 10, -8, -1], [-19, -12, [[-19, [7, [[], -8, -8, [9, -17, 4, [-19, -11, [], -20]]]]], -12, 3, 18], -3], -14, 17, [], 8, 6, -8, -10, 5, 11, [10, 16, [-18, -11, [[-16, 0], 2], 3], -5], 15, [-5, -4], -5, 8, 19, -6, 12, -17, 13, -1, -12] 
print(same_structure_as(og, ot ))