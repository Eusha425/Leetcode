# implemented in bubblesort, not optimised but accepted - need to work on it by utilising a much more optimal algorithm

def sort(nums):
    temp = 0
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    return nums

# a faster implementation of O(n) using a counting sort as stated in the hints
def sort_hint(nums):
    zeros = 0
    ones = 0
    twos = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zeros += 1
        elif nums[i] == 1:
            ones +=1
        else:
            twos += 1
    for i in range(zeros):
        nums[i] = 0
    for i in range(zeros, zeros + ones):
        nums[i] = 1
    for i in range(zeros + ones, zeros + ones + twos):
        nums[i] = 2

    print(nums)

seq = [2,0,2,1,1,0]
print(sort(seq))

print(sort_hint(seq))


