string = input("Enter a String: ")
lowercase_result = ""
for char in string:
    if 'A'<=char<='Z':
        lowercase_result += chr(ord(char)+32)
    else:
        lowercase_result += char
print(f"Lowercase String: {lowercase_result}")

