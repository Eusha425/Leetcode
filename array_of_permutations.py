# 1920. Build Array from Permutation
# Date: 9/12/2023

def buildArray(nums):
    ans = list()
    for i in range(len(nums)):
        ans.append(nums[nums[i]])

    return ans
    

nums = [0,2,1,5,3,4]
print(buildArray(nums))