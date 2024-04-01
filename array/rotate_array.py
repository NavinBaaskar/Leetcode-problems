
def rotate(nums, k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    n = len(nums)
    print(k)
    nums[:n - k] = nums[:n - k][::-1]

    nums[n - k:] = nums[n - k:][::-1]

    nums[:] = nums[::-1]


nums = [1, 2, 3, 4, 5, 6, 7]
k = -3
rotate(nums, k)
print("Rotated array:", nums)