# Parent 1

class father:
    dad = ''

    def dad(self):
        print(self.dad)


# Parant 2
class mother:
    mom = ""

    def mom(self):
        print(self.mom)


# Parant 3
class child:
    son = ""

    def son(self):
        print(self.son)


# child

class sayHello(father, mother, child):

    def sayHi(self):
        print(self.dad, self.mom, self.son)


## Object
obj = sayHello()
obj.dad = 'Nag'
obj.mom = 'Amala'
obj.son = 'Chaithu'

obj.sayHi()

