# 88. Merge Sorted Array
# Date: 31 December 2023

def merge(nums1, nums2):

    temp = []
    for i in range(len(nums2)):

        if nums1[i] < nums2[i]:

        
            temp.append(nums1[i])
        elif nums1[i] == nums2[i]:

            temp.append(nums2[i])
    for i in range(len(nums2)):
        if nums2[i] > nums1[i]:
            temp.append(nums2[i])
    nums1[:] = []
    nums1[:] = temp
    for i in range(len(nums1) -1 ):
        for j in range(len(nums1) - 1):
            if nums1[j] > nums1[j + 1]:
                nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j] 
    """ if nums1[0] == 0:
        nums1.pop(0) """
    print(nums1)

nums1 = [1]
nums2 = []
merge(nums1, nums2)
