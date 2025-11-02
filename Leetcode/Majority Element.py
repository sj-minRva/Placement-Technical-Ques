#Hash Map
#Dictionary

def majorityElement(nums):
    nums.sort()
    print(nums)
    
    Counter = {}
    n = len(nums)
    print(n)
    
    for i in range(n):
        if nums[i] in Counter:
            Counter[nums[i]]+= 1
        else:
            Counter[nums[i]] = 1

    print("Counter: ", Counter)


    for key, count in Counter.items(): 
        if count > n//2:
            return key
    

nums = [2,2,1,1,1,2,2]
result = majorityElement(nums)
print(f"{result} is Majority Element." )
