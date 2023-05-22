class Stack:
    def __init__(self,elemn):
        self.elemn=elemn
    def add_to_stack(self,value):
        self.elemn.append(value)
        
    def reverse(self,l):
        for i in range(len(self.elemn)):
            l.append(self.elemn.pop())
        return l
    
    def is_full(self):
        if self.elemn[0] is not None:
            return 'The stack is full'
        else:
            return 'The stack is not full'
        
    def is_empty(self):
        if len(self.elemn)==0:
            return 'The stack is empty'
        else:
            return 'The stack is not empty'
        
s1=Stack([])
s1.add_to_stack(1)
s1.add_to_stack(2)
s1.add_to_stack(3)

print(s1.is_full())
print()
print(s1.is_empty())
print()
print(s1.reverse([]))





