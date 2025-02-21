string = input("Enter a String: ")
uppercase_result = ""
for char in string:
    if 'a'<=char<='z':
        uppercase_result += chr(ord(char)-32)
    else:
        uppercase_result += char
print(f"Uppercase String: {uppercase_result}")

