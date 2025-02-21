def is_prime(num):
    if num<2:
        return false
    for i in range (2,int(math.sqrt(num))+1):
        if num%i==0:
            return false
        return true
def check_sqrt_prime(n):
    sqrt_n=int(math.sqrt(n))
    return is_prime(sqrt_n)
n=int(input("enter the number"))

sqrt_n=int(math.sqrt(n))
if check_sqrt_prime(n):
    print("the square root of{n},which is{sqrt},is prie number")
else:
    print("the square root of{n},which is{sqrt},is prie number")
