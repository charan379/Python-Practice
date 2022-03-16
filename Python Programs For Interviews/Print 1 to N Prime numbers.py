# Print  1 to N Prime numbers

n = int(input('Enter a number : '))
counter = 0
for x in range(2, n+1):
    for i in range(2, x):
        if x % i == 0:
            break
    else:
        counter += 1
        print(x)


print('Number of prime number between 1 and {} are {} : '.format(n, counter))
input()