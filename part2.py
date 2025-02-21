def fibo_number():
    length=10

    x=0
    y=1
    iteration=0
    if length<=0:
        print("please provide number greater than 0")
    elif length==1:
        print("the fibonocci sequence has{} alement".format(length),":")
        print(x)
    else:
        print("the fibonocci sequence has{} alement".format(length),":")
    while(iteration<length):
        print(x,end=',')
        z=x+y
        x=y
        y=z
        iteration+=1
fibo_number()
