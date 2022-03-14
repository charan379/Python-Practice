import math

x = 3
# Method 1
print(math.factorial(x))

# While Loop
w_x = x
factorial = 1
while w_x != 0:
    factorial *= w_x
    w_x -= 1
print(factorial)

# For loop
f_x = x
factorial_for = 1
for num in range(1, f_x + 1):
    factorial_for *= num
    num -= 1
print(factorial_for)
