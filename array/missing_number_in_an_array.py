def missing_number(nums) -> int:
    n = len(nums)

    total_sum = n * (n + 1) // 2
    sum1 = 0
    for i in range(n):
        sum1 = sum1 + nums[i]

    return total_sum - sum1

def missing_number2(nums):
    n = len(nums)
    xor1 = 0
    xor2 = 0
    for i in range(n):
        xor1 = xor1 ^ i
        xor2 = xor2 ^ nums[i]
    xor1 = xor1 ^ n

    return xor1 ^ xor2


print(missing_number2([0,1, 2, 4, 5]))
