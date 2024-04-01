from typing import *

def swap(left,right,nums):
    temp = nums[left]
    nums[left] = nums[right]
    nums[right] = temp

def reverseArray_helper(left,right,nums):
    if left >= right:
        return nums
    swap(left,right,nums)
    left += 1
    right -= 1
    reverseArray_helper(left,right,nums)

    return nums


def reverseArray(n: int, nums: List[int]) -> List[int]:
    # Write your code here
    left = 0
    right = n - 1
    return reverseArray_helper(left,right,nums)
    

nums = [1,2,4,5,6]
print(reverseArray(len(nums),nums))