def sortedArray(a, b) :
    # Write your code here
    union = []
    n1 = len(a)
    n2 = len(b)

    i = 0
    j = 0

    while i < n1 and j < n2:
        if a[i] <= b[j]:
            if a[i] not in union:
                union.append(a[i])
            i += 1    
        else:
            if b[j] not in union:
                union.append(b[j])        
            j += 1

    while i < n1:
        if a[i] not in union:
            union.append(a[i])
        i += 1

    while j< n2:             
        if b[j] not in union:
            union.append(b[j]) 
        j += 1

    return union            


print(sortedArray([1,2,3,4,6],[2,3,5]))