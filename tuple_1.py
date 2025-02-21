# Modify an element of a tuple.

tuple1 = (1,2,3,4,5,6,7,8,9,10)
list1 = list(tuple1)
list1[0]=0
tuple1=tuple(list1)
print(tuple1)
