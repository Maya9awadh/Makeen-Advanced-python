
def binary(x):
    low=0
    high=x
    
    while low<=high:
        mid=(low+high)//2
        if mid==(x**(0.5)):
            return mid
            break
        elif (x**(0.5) )<mid:
            high=mid-1
            
        else:
            low=mid+1
    return -1

x=int(input('Enter positive number:'))
print(binary(x))