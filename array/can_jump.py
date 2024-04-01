def can_jump_help(nums,i):
        if i >= len(nums) - 1:
            return True
        for j in range(nums[i],0,-1):
            print(i+j+1)
            value = can_jump_help(nums,i + j)
            if value == True:
                return True
        return False


def canJump(nums) -> bool:
    i = 0

    value = can_jump_help(nums, i)

    return value


def canJump_alternate(nums) -> bool:
    reachable = 0

    for i in range(len(nums)):

        if reachable >= len(nums) - 1:
            return True
        if i > reachable:
            return False

        reachable = max(reachable, i + nums[i])

    return True


nums = [2,0]

print(canJump(nums))


