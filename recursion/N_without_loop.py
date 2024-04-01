from typing import List

def print_s(x,count,some_list):
    if count == x:
        return  
    count += 1
    some_list.append(count)
    print_s(x,count,some_list)   
    return some_list 

def printNos(x: int) -> List[int]: 
    # Write your code here
    count = 0
    some_list = []
    
    return print_s(x,count,some_list)


print(printNos(5))