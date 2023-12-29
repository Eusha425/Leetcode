# 53. Maximum Subarray
# Date: 29 December 2023

# brute force method, solves the test case but takes a long run time so solution does not get submitted
def maxSubArray(nums):
    
    max = -99999
    
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total = total + nums[j]
            if total > max:
                max = total

    print(max)

# implementing the solution according to kanade's algo (https://en.wikipedia.org/wiki/Maximum_subarray_problem)
# the algo states that we have two pointers/variables that keep on updating upon each iteration so that we only need one loop

def maxSubArrayKanade(nums):
    # Initialize max to the smallest possible integer. This variable will keep track of the maximum subarray sum we've encountered so far.
    max = -99999 
    # Initialize total to 0. This variable represents the current subarray sum.
    total = 0 
    # Iterate over the array.
    for i in range(len(nums)): 
        # Add the current element to total.
        total = total + nums[i] 
        # If total is greater than max, update max. This means we've found a subarray with a larger sum.
        if total > max: 
            max = total
        # If total is less than 0, reset it to 0. This is because a negative sum would decrease the sum of a future potential subarray.
        # For example, consider an array [-2, 3]. Even though -2 + 3 = 1, the maximum subarray sum is 3, not 1. So, we reset total to 0 whenever it becomes negative.
        if total < 0: 
            total = 0
    # After iterating over the entire array, max will hold the maximum subarray sum.
    return max


arr = [-2,1,-3,4,-1,2,1,-5,4]
maxSubArray(arr)
