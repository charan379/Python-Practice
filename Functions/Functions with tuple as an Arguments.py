# Functions with any number of arguments

# Define a function

# Function Sum of values
def Sum(values):
    result = 0
    for x in values:
        result += x
    return result


# Function to get a valid integer

def GetValidtNum():
    num = input("Enter a number : ")
    while not num.isnumeric():
        print(f'{num} is not an Integer ')
        num = input("Enter a number : ")
    return int(num)


def GetNums():
    nums = []
    n = GetValidtNum()
    nums.append(n)
    print(f'Your Numbers for arithmetic operations are: {nums}')
    choice = input("Do ypu want to add more numbers , or want to show result of operation \n"
                   "Enter a number to add or press any key to show result :  ")
    while choice.isnumeric():
        nums.append(int(choice))
        print(f'Your Numbers for arithmetic operations are: {nums}')
        choice = input("Do ypu want to add more numbers , or want to show result of operation \n"
                   "Enter a number to add or press any key to show result :  ")
    return tuple(nums)


# Calling a function

numbers = GetNums()

add_result = Sum(numbers)

print(f"Sum of {numbers} is : {add_result}")