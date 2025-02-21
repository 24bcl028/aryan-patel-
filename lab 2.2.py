a = int(input("enter number: "))
b = int(input("enter number: "))
c = int(input("enter number: "))
if (a>b and a>c):
        if(b>c):
                print(a,"is largest",c,"is smallest")
        else:
                print(a,"is largest",b,"is smallest")
if (b>a and b>c):
        if(a>c):
                print(b,"is largest",c,"is smallest")
        else:
                print(b,"is largest",a,"is smallest")
if (c>a and c>b):
        if(a>b):
                print(c,"is largest",b,"is smallest")
        else:
                print(c,"is largest",a,"is smallest")
