## There will two types of variables classes
##  1) Instance 2) class/static variables

class tv:
    ## Class or Static Variables are written here
    brand = "ONIDA"

    def __init__(self):
        ## Instance variables are written here
        self.inches = 'inches'
        self.type = 'type'
        self.hdmi = 'hdmi'

    def info(self):
        ## Displays TV Info
        print(f'Brand   : {self.brand}')
        print(f'Inches  : {self.inches}')
        print(f'TV Type : {self.type}')
        print(f'HDMI    : {self.hdmi}')

    ## Types of methods in class
    ## 1 ) Instance Methods
    # 1 ) set Method
    def set_properties(self, inches, type, hdmi):
        self.inches = inches
        self.type = type
        self.hdmi = hdmi

    # 2 ) Get Method
    def get_properties(self):
        return self.inches, self.type, self.hdmi

    ## 2 ) Class Methods
    # 1) Get Method
    @classmethod
    def get_brand(cls):
        return cls.brand

    # 2) Set Method
    # @classmethod
    ##  Set Method for class variable is not available since it's a static variable

    @staticmethod
    def greet():
        print("Hi Enjoy programing")

    global SayHi
    def SayHi(self):
        print(" Hello")



tv1 = tv()
# set_properties of tv1
tv1.set_properties(32,'Smart TV','yes')
tv1.brand = "TCL"
# Display properties of tv1 using info() Method in class
tv1.info()

# get_properties of tv1 using get method
inc , ty, hdmi = tv1.get_properties()
# print properties
print(inc,ty,hdmi)

# Get Brand name using get_method in @classmethods
# we should call @classmethods only with class names
# using class
print(f'{tv.get_brand()}')

# this is using object
print(f'{tv1.brand}')


# Calling a static method in class using object
# using object
tv1.greet()
# using class
tv.greet()

# as a global function
SayHi()