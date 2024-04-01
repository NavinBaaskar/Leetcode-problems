

    
def removeElement(nums, val: int) -> int:
    swap = True
    for i in range(len(nums)):
            
        if nums[i] == val:
                
            swap = False
            for j in range(i+1,len(nums)):
                if nums[j] != nums[i]:
                        
                    swap = True
                    nums[i],nums[j] = nums[j],nums[i]
                    break

        if swap == False:
            return i

nums = [3,2,2,3]
val = 3

element = removeElement(nums, val)
print(element)
print(nums)