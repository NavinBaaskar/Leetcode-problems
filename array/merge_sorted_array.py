def merge(nums1, m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = 0
    j = 0
    end_ptr = m
    arr2 = []

    while i < m + n and n != 0 and j < n:
        # print(i)
        # if i >= m and nums1[i] == 0 and nums2[j] != 0:
        #     nums1[i] = nums2[j]
        #     i += 1
        #     j += 1

        if nums1[i] <= nums2[j]:
            i += 1
        else:
            nums1.insert(i, nums2[j])
            end_ptr += 1
            arr2.append(j)
            nums1.pop()
            j += 1
            i += 1

    print(nums1, end_ptr)
    while end_ptr < m + n and j < n:
        nums1[end_ptr] = nums2[j]
        j += 1
        end_ptr += 1

    if m == 0:
        nums1[0] = nums2[0]


nums1 = [1, 2, 3, 0, 0, 0]

m = 3

nums2 = [2, 5, 6]

n = 3

merge(nums1, m, nums2, n)

print(nums1)
