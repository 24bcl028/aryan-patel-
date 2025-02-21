#Problem1
list1=["shreya",("Jaitin",),("jeel","shreyash"),"krupa"]
boys = sum(len(name) for name in list1 if isinstance(name,tuple))
girls = sum(1 for name in list1 if isinstance(name,str))
print(f"Number of Boys: {boys}\nNumber of Girls: {girls}")
