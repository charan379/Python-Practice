# Count the number of digits in a string

str = 'charan2tej1a379'

count_digit = 0
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for x in str:
    if x in digits:
        count_digit += 1
# for x in str:
#     if x.isdigit():
#         count_digit += 1

print(count_digit)