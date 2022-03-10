# lambda is an anonymous function that can take any number of arguments but can perform a single action or can have a
    # single expression

# lambda example

#To add two numbers
k = lambda a=1,b=2 : a+b
print(k())

#To get true or false
boll = lambda a=1: a % 2 == 0

print(boll())
