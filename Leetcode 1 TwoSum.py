#Two Sum Problem Leetcode 1

def twoSum(nums,target):
    map = {}
    for i in range(0,len(nums),1):
        diff = target-nums[i]
        if(diff in map):
            return [map[diff],i]
        else:
            map[nums[i]]=i
    return   


print(twoSum([2,7,11,15],9))
