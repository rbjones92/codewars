# Robert Jones
# 8.23.22
# CodeWars - Pick Peaks - https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/train/python
# Example pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3] should return {pos: [3, 7], peaks: [6, 3]}


### Online Clever Solution ### 
def pick_peaks(arr):
    peak, pos = [], []
    res = { "peaks":[], "pos":[] }
    
    for i in range(1, len(arr)) :
        if arr[i]>arr[i-1] :
            peak, pos = [arr[i]], [i]
        
        elif arr[i]<arr[i-1] :
            res["peaks"] += peak
            res["pos"] += pos
            peak, pos = [], []
    
    return res


print(pick_peaks([1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3]))
