# Fibonacci Series

n = int(input('Enter a number : '))

num1 = 0
num2 = 1
for x in range(1, n):
    if num1 == 0:
        print(num1)
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    if num3 >= n:
        break
    print(num3)


