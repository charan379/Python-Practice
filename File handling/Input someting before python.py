file = open('data.txt', 'r')
lines = file.readlines()

ln = 0
i = 0
for line in lines:
    if 'Python' in line:
        ln = i
        lines[i] = 'IMP : ' + lines[i]
    i += 1

file.close()

# write

file = open('data.txt', 'w')
file.writelines(lines)