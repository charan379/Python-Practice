# Reverse a given number
def reverseNum(num):
    original_num = num
    reversed_num = 0
    while num > 0:
        last_digit = num % 10
        reversed_num = reversed_num*10 + last_digit
        num = num // 10

    print(f'Reverse of number {original_num} is {reversed_num}')
    # print(reversed_num)


reverseNum(12345)

#
# for x in range(0, 101):
#     reverseNum(x)