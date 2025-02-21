#Accept two string. Check whether one string is there in another string.

str1 = input("Enter a string: ")
str2 = input("Enter another String: ")
found = False

for i in range(len(str1) - len(str2) +1):
    if str1[i:i+len(str2)] == str2:
        found = True
        break
if found:
    print(f" '{str2} is present in '{str1}' ")
else:
        print(f" '{str2}' is not present in '{str1}' ")
