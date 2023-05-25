import sys
lst=[1,2,3]

print(sys.getsizeof(lst))
value=iter(lst)
for i in range(len(lst)):
    print(next(value))

def fun2():
    yield 1
print(next(fun2()))