# print even numbers only from a dictionary
def GetEven(listArg):
    list_of_evens = []
    for x in listArg:
        if x % 2 == 0:
            #print(x)
            list_of_evens.append(x)
    return list_of_evens

#Calling GetEven()
li = [1, 3, 2, 4, 6, 8, 54, 88, 62]
even_li = GetEven(li)
print(even_li)

# Using lambda and filter function

print('Using lambda and filter function')

get_evens = set(filter(lambda x : x % 2 == 1, range(0,100)))
print(get_evens)


