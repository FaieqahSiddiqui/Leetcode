
# Leetcode 26 Remove Duplicates from Sorted Array

def removeDuplicates(nums):
    if(len(nums)==0):
        return 0

    l=1
    for i in range(1,len(nums)):
        if(nums[i] == nums[i-1]):
            continue
        else:
            nums[l]=nums[i]
            l+=1

    return l
    
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
