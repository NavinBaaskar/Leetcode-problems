def majorityElement(nums) -> int:
    max_count = 0
    max_element = 0
    som_dict = {}
    for i in range(len(nums)):
        if nums[i] in som_dict:
            som_dict[nums[i]] += 1
        else:
            som_dict[nums[i]] = 1
        if max(max_count, som_dict[nums[i]]) == som_dict[nums[i]]:
            max_element = nums[i]
            max_count = som_dict[nums[i]]
    return max_element



def majorityElement_alternate(nums):
    n = len(nums)
    som_dict = {}
    for i in range(len(nums)):
        if nums[i] in som_dict:
            som_dict[nums[i]] += 1
        else:
            som_dict[nums[i]] = 1
        if som_dict[nums[i]] > n / 2:
            return nums[i]


max_element = majorityElement([3,2,3])
print(max_element)