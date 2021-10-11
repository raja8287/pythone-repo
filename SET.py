
list_l=[21,2,12,1,21,2,13,4,2]
s_from_list=set(list_l)
print(s_from_list)#only print unique value (not gona repeat the same element
print(type(s_from_list))
#set only add unique elements
s_from_list.add(2)#not gona add 2 in set bcz 2 is already present
s_from_list.add(9)#adding 9 bcz it is unique
print(s_from_list)