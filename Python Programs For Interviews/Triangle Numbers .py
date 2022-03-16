# Triangle numbers

# Print Triangular number with 1 to N adders
def one_to_n_series():
    num = int(input('Enter a number : '))
    li = []
    base_num = 0
    for x in range(0, num + 1):
        base_num += x
        li.append(base_num)
    return li


# Check if an given number is tiangular or not
def tri_or_not():
    num = int(input('Enter a number : '))
    tri_sum = 0
    for x in range(0, num + 1):
        tri_sum += x
        if num == tri_sum:
            print(num, 'Is a Triangular number ')
            break
        elif x == num:
            print(num, 'Is not Triangular number')

# Print Triangular Numbers in 0 to n

def zero_to_n():
    num = int(input('Enter a number : '))
    for n_num in range(1, num + 1):
        tri_sum =0
        for x in range(1, n_num + 1):
            tri_sum += x
            if tri_sum == n_num:
                print(n_num)
                break
            if x == n_num:
                break


zero_to_n()

