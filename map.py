
#convert the word in list to upper case
name=input("please enter the name: ")
print()
names=[]
while name!='':
    names.append(name)
    name=input("please enter the name:")
    print()
new_name=list(map(lambda x: x.upper() ,names))
print(new_name)