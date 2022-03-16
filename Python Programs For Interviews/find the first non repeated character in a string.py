# Find the first non-repeated character in a string

str = 'charanchrn'

length = len(str)

for x in range(length):
    count_of_char = 0
    for i in str:
        if i == str[x]:
            count_of_char += 1
    if count_of_char == 1:
        print(str[x])
        break
else:
    print('There are no repeated characters')

# for x in str:
#     if str.count(x) == 1:
#         print(x)
#         break
