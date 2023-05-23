def insertion_sort(array):
    for step in range(1,len(array)):
        key=array[step]
        j=step-1
        
        while j>=0 and key<array[j]:
            array[j+1] =array[j]
            j=j-1
        array[j+1]=key
    return array
l=['Said,25','Majid,19','Salim,32','Ali,21','Sultan,28']
age=[]
for i in l:
    data=i.split(',')
    age.append(int(data[1]))

print(insertion_sort(age))

s=[]
for a in range(len(age)):
    for j in range(len(l)):
        data=l[j].split(',')
        if age[a]==int(data[1]):
            s.append(data[0])
print(s)
        
