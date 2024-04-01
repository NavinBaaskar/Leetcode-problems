def check(nums) -> bool:
    decre = 0
    if len(nums) <= 2:
        return True

    for i in range(1, len(nums)):

        if nums[i] < nums[i - 1]:
            decre += 1

        if decre > 1:
            return False

    if nums[0] < nums[-1]:
        decre += 1

    if decre > 1:
        return False
    return True


print(check([2,1,3,4]))
        
            