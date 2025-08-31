
def removeElement(nums, val):
    k = 0
    length = len(nums)
    for i in range(len(nums)):        
        if nums[i] != val:
            k+=1

    return k

nums = [0,1,2,2,3,0,4,2]
val = 2
removeElement(nums, val)
        
