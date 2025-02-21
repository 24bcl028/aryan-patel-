
string = input("Enter a String: ")
countalpha = 0
countnum = 0
for i in string:
    if(i>='a' and i<='z'):
        countalpha+=1
    if(i>='A' and i<='Z'):
        countalpha+=1
    if(i>='0' and i<='9'):
        countnum+=1
print("Alphabets: ",countalpha)
print("Digits: ",countnum)
