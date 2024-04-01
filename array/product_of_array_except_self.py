def productExceptSelf(nums):
    n = len(nums)
    prefix_product = 1
    postfix_product = 1
    result = [0] * n
    for i in range(n):
        result[i] = prefix_product
        prefix_product *= nums[i]
    for i in range(n - 1, -1, -1):
        result[i] *= postfix_product
        postfix_product *= nums[i]
    return result


print(productExceptSelf(nums = [1,2,3,4]))