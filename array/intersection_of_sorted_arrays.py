from os import *
from sys import *
from collections import *
from math import *

def findArrayIntersection(arr: list, n: int, brr: list, m: int):
    i = 0
    j = 0
    ans = []
    while i < n and j < m:
        if arr[i] > brr[j]:
            j += 1
        elif brr[j] > arr[i]:
            i += 1
        else:
            ans.append(arr[i])
            i += 1
            j += 1
    
    return ans
