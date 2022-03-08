# Functions with two arguments

# Creating a function
def addsub(fn, sn):
    resultadd = fn + sn
    resultsub = fn - sn
    return resultadd, resultsub

def GetNum():
    num = input("Enter a number: ")
    while not num.isnumeric():
        print(f'{num} is not a number ')
        num = input("Enter a number: ")
    return num


# Calling a function
print("Enter First Number")
n1 = int(GetNum())
print("Enter Second Number")
n2 = int(GetNum())
sum, sub = addsub(n1,n2)

print(f'Sum of {n1},{n2} : {sum}')

print(f'Sub of {n1},{n2} : {sub}')