#list can be a particular data type and can be mix data type
list01=["raja","nisha","soni","arbo",35,28.3]
print(list01)
num=[2,3,41,3,5,4,30,4]
#this function is use for sorting the intiger list
"""num.sort()
print(num)
#it will reverse the sorted array and unsorted
num.reverse()
print(num)"""
#for assessing  any element for the list after sorting
#as our requirdment sorted or not
print(num[4])
#this is use for taking a element from a point to another point

print(num[1:])#ending point is last of index by default (if not given)
print(num[:3])#starting point is 0 by default(if not given)
print(num[2:4])#starting point is 2 and ending point is 4
print(num[::2])#for jumping the element [2,3,41,3,5,4,30,4]<===>[2,41,5,30]

#for adding the number in a list
num.append(9)
print(num)
#for inserting a particular number to a particular place
num.insert(2,11)
print(num)
#for removing a particular number only
num.remove(11)
print(num)
#imutable function
#tp is tuple function
tp=(1,2,3)#tuple conssits of more than one elements
print(tp)