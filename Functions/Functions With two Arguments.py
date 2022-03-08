# Functions with two arguments

# Creating a function
def sum(fn, sn):
    result = fn + sn
    return result

def GetNum():
    num = input("Enter a number: ")
    while not num.isnumeric():
        print(f'{num} is not a number ')
        num = input("Enter a number: ")
    return num


# Calling a function
print("Enter First Number")
n1 = GetNum()
print("Enter Second Number")
n2 = GetNum()
sum = sum(int(n1),int(n2))

print(f'Sum of {n1},{n2} : {sum}')