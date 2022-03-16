a = 'Charan'
b = 'Teja'
print(a, b)
a = a + "," + b
b = a.split(',')[0]
a = a.split(',')[1]

print(a, b)