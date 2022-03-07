## 1 to 100 using single end range only
print('For loop 1 to 100')
for x in range(100):
    print(x)

## 1 to 100 using starting and ending range

for x in range(1, 101):
    print(x)

## 1 to 100 even numbers using increment in range
for x in range(0, 100, 2):
    print(x)

## 1 to 100 odd numbers using increment in range


for x in range(1, 100, 2):
    print(x)

## 1 to 100 even numbers using increment in range and %

for x in range(0, 101):
    if x % 2 == 0:
        print(x)

# 1 to 100 odd numbers using increment in range and %

for x in range(0, 101):
    if x % 2 == 1:
        print(x)


## iterate items of a list using for loop
list1 = ['car', 'bus', 'bike']

for item in list1:
    print(item)

## iterate items of a Dictionary using for loop
dist1 = ['car:Honda', 'bus:tata', 'bike:Hero']

for item in dist1:
    print(item)