def twoSum( nums, target: int):
    some_dict = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff not in some_dict:
            some_dict[nums[i]] = i
        else:
            return [some_dict[diff], i]


print(twoSum([2,7,11,15],9))