# Matching characters of a string

name = 'telugu'
matching_char = set()
for chr in name:
    if name.count(chr) > 1:
        matching_char.add(chr)

print(matching_char)
for x in matching_char:
    print(x)