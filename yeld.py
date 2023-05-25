def fun2():
    yield 1
print(next(fun2()))

def fibonacci_numbers(nums):
    x,y=0,1
    for i in range(nums):
        x,y=y, x+y
        yield x
        
def square(nums):
    for num in nums:
        yield num**2
        
def triple(nums):
    for num in nums:
        yield num**3

print(sum(triple(square(fibonacci_numbers(10)))))