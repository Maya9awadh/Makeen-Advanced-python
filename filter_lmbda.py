#using filter and lambda to return the word that
#is lower case in list

lst=['maya','Maya','hello','HELLO']

new_lst=list(filter(lambda x: x.islower(),lst))

print(new_lst)
