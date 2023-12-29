# 118. Pascal's Triangle

def generate(numRows: int):
    sub_array = []
    main_array = [[1]]
    constant = 1 # the constant value of 1 that needs to be added to the beginning and end of the array

    for i in range(1, numRows):
        sub_array = [] # reset the array to an empty one to add it to the main array again
        sub_array.append(constant) # adding 1 to the beginning of the sub array
        for j in range(1, i): # calculate the middle rows except the first and last row as they are always 1
            
            start = main_array[i-1][j-1]
            end = main_array[i-1][j]
            ans = start + end
            sub_array.append(ans)

        sub_array.append(constant) # adding 1 to the end of the sub array
        main_array.append(sub_array) # adding the sub array to the main array

    return main_array

print(generate(5))