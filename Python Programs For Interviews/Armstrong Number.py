num = int(input('Enter a number : '))
num_str = str(num)
power = len(num_str)
num_sum = 0

for x in num_str:
    x_power_val = pow(int(x), power)
    num_sum += x_power_val

if __name__ == '__main__':
    print('Given Number is {} and sum of its digits raised by the power of number of digits is {}'.format(num, num_sum))
    if num == num_sum:
        print(num, 'Is an Armstrong number')
    else:
        print(num, 'is not an Armstrong number')
