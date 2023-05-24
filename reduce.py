from functools import reduce
lst=[1,2,3,4,6]
sum_l=reduce(lambda x,y:x+y**2,lst)
print(sum_l)