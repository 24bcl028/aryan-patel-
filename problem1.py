#Count how many vowels are there in a String
string = input("Enter a String: ")
vowels = "aeiouAEIOU"
count = 0

for char in string:
    if char in vowels:
        count += 1
print(f"Number of vowels in String are: {count}")
        
