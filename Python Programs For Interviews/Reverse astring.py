x = '153'
# Method 1
print(x[::-1])

# Method 2 For Loop
reverse = ''
last_index = len(x) - 1
for char in range(-1, last_index):
    reverse += x[last_index]
    last_index -= 1
print(reverse)

# Method 3

reverse = ''

for char in x:
    reverse = char + reverse
print(reverse)

