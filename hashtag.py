# Robert Jones
# 8.30.22
# CodeWars - The Hashtag Generator - https://www.codewars.com/kata/52449b062fb80683ec000024/train/python



string = 'codewars is nice'

import re


def generate_hashtag(s):
    s = s.strip()
    s = list(s)

    if s:

        s = [x.lower() for x in s]
        s[0] = s[0].upper()

        for i in range(0,len(s)):

            if s[i] == ' ':
                s[i+1] = s[i+1].upper()

        s = "".join([str(i) for i in s])
        
        pattern = re.compile(r'\s+')
        s = re.sub(pattern, '',s)
        print(f'#{s}')

        if len(s) <= 140:
            return(f'#{s}')

        else:
            return False
    
    else:
        return False


generate_hashtag(string)