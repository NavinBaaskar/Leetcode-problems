def getSecondOrderElements(n: int,  a):
    # Write your code here.
    largest = a[0]
    smallest = a[0]

    sec_largest = -1
    sec_smallest = float('inf')

    for i in range(1,len(a)):
        if a[i] > largest:
            sec_largest = largest
            largest = a[i]
        elif a[i] != largest and a[i] > sec_largest:
            sec_largest = a[i]
        if a[i] < smallest:
            sec_smallest = smallest
            smallest = a[i]    
        elif a[i] < sec_smallest and a[i] != smallest:
            sec_smallest = a[i]
   
   

    return [sec_largest,sec_smallest]        



print(getSecondOrderElements(5,[7,4,8,2,3]))