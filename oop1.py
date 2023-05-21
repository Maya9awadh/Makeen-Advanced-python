class Pearson:
    num_person=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Pearson.num_person +=1
    def __str__(self):
        return "This person name is {} and {} years ols".format(self.name,self.age)
    def set_age(self,age):
        self.age=age
    def set_name(self,name):
        self.name=name
P1=Pearson('Ahmed',22)
P2=Pearson('A',92)
P2.set_age(42)
print(P2.__str__())
print(Pearson.num_person)