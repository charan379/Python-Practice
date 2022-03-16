str1 = str(input("Enter string : "))
char1 = str(input("Enter char : "))


counter = 0

for x in str1:
    if x == char1:
        counter += 1

print(counter)