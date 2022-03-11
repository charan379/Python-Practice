# open file

file = open('data.txt', 'r')
data = file.read()
file.close()

# write file

file2 = open('data2.txt', 'w')
data2 = data
file2.write(data2)
file2.close()