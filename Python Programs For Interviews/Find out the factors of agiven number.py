# Find out given number is prime number or not

x = int(input('Enter a number : '))

for num in range(1, x+1):
    if x % num == 0:
        print(num)