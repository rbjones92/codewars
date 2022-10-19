# Robert Jones
# 8.23.22
# CodeWars - Pick Peaks - https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/train/python
# Example pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3] should return {pos: [3, 7], peaks: [6, 3]}



# Working Solution
def pick_peaks(arr):

    test = arr
    test_copy = test.copy()

    new = []
    prev = []
    dups = []

    for c in range(0,len(test),1):
        if len(new) == 0:
            new.append(test[c])
            prev = test[c]
        if test[c] == prev:
            dups.append(c)
        else:
            new.append(test[c])
            prev = test[c]

    dups = dups[1:]

    tops = []
    for i in range(1,len(new)-1,1):
        if new[i] > new[i+1] and new[i] > new[i-1]:
                tops.append(i)
            

    for i in range(0,len(dups),1):
        for j in range(0,len(tops),1):
            if tops[j] >= dups[i]:
                tops[j] = tops[j] + 1 


    peaks = []
    for i in range(0,len(tops),1):
        peaks.append(test_copy[tops[i]])
    

    my_dict = {'pos':tops , 'peaks':peaks}

    return my_dict


    
print(pick_peaks([1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3]))
