# 1929. Concatenation of Array
# Date: 9/12/2023

def getConcatenation(nums):
    ans = list()

    for j in range(2):
        for i in range(len(nums)):
            ans.append(nums[i])

    return ans

nums = [1,2,1]
print(getConcatenation(nums))