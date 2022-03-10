x = 10
y = 20
z = 30


def add(*v):
    # here x , y, z are global variables
    # making result a global
    global result
    result = x + y + z
    return result


add()
# here result is only declared in local function add()
print(result)


def printGloblas():
    hkl = 0
    # get hkl
    for k, v in globals().items():
        if hkl < len(k):
            hkl = len(k)

    # make printing format with hkl
    for key, value in globals().items():
        if hkl == len(key):
            print(f'{key} : {value}')
        else:
            space = ''
            bal_space = hkl - len(key)
            for x in range(bal_space):
                space += ' '
            print(f'{key + space} : {value}')


printGloblas()
print(type(globals()))