# base class

class father:
    dad = ''

    def dad(self):
        print(self.dad)


# Intermediate Class 1
class mother(father):
    mom = ""

    def mom(self):
        print(self.mom)


# Intermediate Class 2
class child(mother):
    son = ""

    def son(self):
        print(self.son)


# child / Derived Class

class sayHello(child):

    def sayHi(self):
        print(self.dad, self.mom, self.son)


## Object
obj = sayHello()
obj.dad = 'Nag'
obj.mom = 'Amala'
obj.son = 'Chaithu'

obj.sayHi()
