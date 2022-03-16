# Find out given number is prime number or not

x = int(input('Enter a number : '))

for num in range(2, x):
    if x % num == 0:
        print(num)
        break