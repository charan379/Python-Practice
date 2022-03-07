#while loop

# 1 to 100 Numbers
print("1 to 100")
c = 1
while c <= 100:
    print(c)
    c+=1

# 1 to 100 complicated
print("100 to 1 ")
c = 100
while c <= 100:
    print(c)
    c -= 1
    if c == 0:
        break

# Odd number upto 100

print(" Odd Numbers")
c = 1
while c <= 100:
    print(c)
    c+=2

# Even number upto 100

print(" Even Numbers")
c = 2
while c <= 100:
    print(c)
    c+=2

# even number by %2

c = 0
print("Odd number by %2")
while c <= 100:
    if c % 2 == 1:
        print(c)
    c += 1

# Math table using while loop

table = 2
print(" math table ")
c = 1
while c <= 10:
    print(f'{table} * {c} = {table*c}')
    c += 1
