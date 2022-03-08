## *args

def myFunc(*values):
    result = 0
    for x in values:
        result += x
    print(values)
    return result


sum = myFunc(2,3,1,3,5,4,3,3,65,76)

print(sum)