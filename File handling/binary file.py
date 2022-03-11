file = open('IDU.jpg', 'rb')
data = file.read()
file.close()


file2 = open('ii.jpg', 'wb')
file2.write(data)
file2.close()