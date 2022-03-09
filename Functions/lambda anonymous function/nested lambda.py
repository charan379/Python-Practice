# Nested lambda functions

sum3 = lambda a : (lambda b : lambda c : a+b+c)

print(sum3(1)(1)(1))

