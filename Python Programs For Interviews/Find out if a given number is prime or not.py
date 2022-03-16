# Finding out if a given number is prime or not

number = int(input('Enter a number : '))
factors = []

# for x in range(2, number):
for x in range(1, number + 1):
    if number % x == 0:
        #print('Not a prime number ')
        #break
        factors.append(x)
# else:
#     print('Prime')

if len(factors) > 2:
    print(number, 'Given Number is divisble by more the 2 natural numbers : ', factors)
    print('So,', number, 'Is not a prime number')
else:
    print(number, 'Is Only Divisible by ', factors, '\n So, its an prime number')