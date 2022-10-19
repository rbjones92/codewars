# Robert Jones
# 8.30.22
# CodeWars - soduku - https://www.codewars.com/kata/529bf0e9bdf7657179000008/train/python


def valid_solution(board):

    sol = set([1,2,3,4,5,6,7,8,9])
    
    for i in range(0,len(board)):
        print((list(zip(*board))[i]))
        if set(board[i]) and set(list(zip(*board))[i]) == sol:
            continue
        else:
            return False

    temp = []
    temp_1 = []
    temp_2 = []
    for j in range(0,len(board),1):
        temp.append(board[j][0:3])
        temp_1.append(board[j][3:6])
        temp_2.append(board[j][6:9])
        if len(temp_2) == 3:
            temp = [item for sublist in temp for item in sublist]
            temp_1 = [item for sublist in temp_1 for item in sublist]
            temp_2 = [item for sublist in temp_2 for item in sublist]
            if set(temp) and set(temp_1) and set(temp_2) == sol:
                temp = []
                temp_1 = []
                temp_2 = []
            else:
                return False
                

    return True



print(valid_solution([  [5, 3, 4, 6, 7, 8, 9, 1, 2], 
                        [6, 7, 2, 1, 9, 5, 3, 4, 8],
                        [1, 9, 8, 3, 4, 2, 5, 6, 7],
                        [8, 5, 9, 7, 6, 1, 4, 2, 3],
                        [4, 2, 6, 8, 5, 3, 7, 9, 1],
                        [7, 1, 3, 9, 2, 4, 8, 5, 6],
                        [9, 6, 1, 5, 3, 7, 2, 8, 4],
                        [2, 8, 7, 4, 1, 9, 6, 3, 5],
                        [3, 4, 5, 2, 8, 6, 1, 7, 9]]))