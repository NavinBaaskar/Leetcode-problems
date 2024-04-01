def removeDuplicates(nums):
    i = 0
    j = 1
    while i < len(nums) and j < len(nums):
        if nums[j] != nums[i]:
            nums[i + 1], nums[j] = nums[j], nums[i + 1]
            i += 1
        j += 1

    return i + 1

nums = [0,0,1,1,1,2,2,3,3,4]
k = removeDuplicates(nums)
print(k, nums)