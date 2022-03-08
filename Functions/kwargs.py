## **kwargs or Arbitrary Keyword Arguments

def myFunc(**data):
    print(data)
    for x, y in data.items():
        ## Here x is Keys and Y is Values
        print(f' {x} : {y}')
       ## print("beautifully")
        # if x == 'Name':
        #     print(f' {x}   : {y}')
        # elif x == 'Age':
        #     print(f' {x}    : {y}')
        # else:
        #     print(f' {x} : {y}')


myFunc(Name='Charan', Gender='Male', Age=23, Mobile='9502116185')
