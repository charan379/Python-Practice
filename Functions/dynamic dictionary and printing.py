#passing dictionary to function as an argument


def myFunc(dict):
    hkl = 0
    for k,v in dict.items():
        if hkl < len(k):
            hkl = len(k)
    for k,v in dict.items():
        if hkl == len(k):
            print(f'{k}:{v}')
        else:
            space = ''
            space_diff = hkl - len(k)
            for x in range(space_diff):
                space += ' '
            print(f'{k+space}:{v}')

# initialize a new empty dictionary

my_dict = {}

choice = '1'
while choice != '0':
    user_key = input("Enter user key : ")
    user_value = input(f'Enter user value for {user_key} : ')
    my_dict[user_key] = user_value
    choice = input("Enter any key to continue or 0 to exit")

myFunc(my_dict)

