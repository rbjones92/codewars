# Robert Jones
# 10.12.22
# Codewars - https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python
# ... Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

def snail(snail_map):
    flat_snail = [item for sublist in snail_map for item in sublist]
    if len(flat_snail) == 0 or len(flat_snail) == 1:
        return flat_snail
    result = []
    run = 0
    side = len(snail_map[0])-1
    cnt_lists = len(snail_map)-1
    x = True
    while x:
        result.append(snail_map[run][run:side])
        result.append(list(el[side] for el in snail_map[run:side]))
        result.append(snail_map[cnt_lists][side:run:-1])
        result.append(list(el[run] for el in snail_map[side:run:-1]))
        run += 1
        side -= 1
        cnt_lists -= 1
        stopper = len(result[-1])

        if stopper == 1 or stopper == 2:
            x = False
    
    result = [item for sublist in result for item in sublist]

    if len(result) != len(flat_snail):
        result.append(flat_snail[int(len(result)/2)])

    return result

print(snail(array))
