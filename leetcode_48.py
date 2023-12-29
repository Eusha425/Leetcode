# 48. Rotate Image
# Date: 29 December 2023
def rotate(matrix):

    length = len(matrix)
    
    # the following lines of code is for transposition, this will swap all the values of rows into columns and vice versa, the result will be a mirrored version of the rotation i.e the 90 degree rotation.
    # example output = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    for i in range(length):
        for j in range(length):
            if i < j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # over here we are reversing each row, so that it is no longer a mirrored version of the rotation but the actual rotation (e.g : [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
    for i in range(length):
        start = 0
        end = length - 1
        while start < end:
            matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
            start +=1
            end -= 1


    print(matrix)

arr = [[1,2,3],[4,5,6],[7,8,9]] # example input


print(arr)
rotate(arr)
