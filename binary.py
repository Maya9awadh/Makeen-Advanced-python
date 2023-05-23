def binary(key,list_):
    l.sort()
    low=0
    high=(len(list_)-1)
    
    while low<=high:
        mid=(low+high)//2
        if list_[mid]==key:
            return mid
            break
        elif key <list_[mid]:
            high=mid-1
            
        else:
            low=mid+1
    return -1

l=[0,1,2,20,3,4,5]
print(binary(20,l))