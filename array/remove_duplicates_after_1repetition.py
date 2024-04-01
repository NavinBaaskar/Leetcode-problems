def removeDuplicates(nums):
    some_dict = {}
    some_dict[nums[0]] = 1
    j = 1

    if len(nums) <= 2:
        return len(nums)

    for i in range(len(nums)):
        if j == len(nums):
            break
        while j < len(nums):
            if nums[i] == nums[j]:
                if nums[j] not in some_dict:
                    some_dict[nums[j]] = 1
                else:
                    some_dict[nums[j]] += 1
                j += 1
            else:

                if nums[j] in some_dict:
                    if some_dict[nums[j]] <= 2:
                        some_dict[nums[j]] += 1
                        if j > i + 2:
                            nums[i + 2], nums[j] = nums[j], nums[i + 2]
                        j += 1
                        break
                else:
                    some_dict[nums[j]] = 1
                    if j > i + 2:
                        nums[i + 2], nums[j] = nums[j], nums[i + 2]
                    j += 1
                    break
    k = 0
    for i in some_dict:
        if some_dict[i] > 2:
            k += 2
        else:
            k += some_dict[i]
    return k

nums = [0,0,1,1,1,2,2,3,3,4]
k = removeDuplicates(nums)
print(k, nums)
