def armstrongNum(n_val):
    counter = 0
    for x in range(0, n_val + 1):
        str_x = str(x)
        power = len(str_x)
        pow_sum = 0
        for i in str_x:
            pow_of_digit = pow(int(i), power)
            pow_sum += pow_of_digit
        if x == pow_sum:
            counter += 1
            print(x, 'Is an Armstrong')
    print('Number of armstrong numbers between 1 to {} are : {} '.format(n, str(counter)))


if __name__ == '__main__':
    n = int(input('Enter N value : '))
    print('Armstrong numbers between 1 to {} are :'.format(n))
    armstrongNum(n)
