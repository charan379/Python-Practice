# base class

class names:
    dad = ''
    mom = ""
    son = ""


# Single Inheritance
class father(names):
    def dadS(self):
        print(self.dad)


# MultiLevel Inheritance
class mother(father):

    def moms(self):
        print(self.mom)


# Multiple Inheritance
class child(mother, father):

    def sonS(self):
        print(self.son)



## Object
names.dad = 'Nag'
names.mom = 'Amala'
names.son = 'Chaithu'

objF = father()
objF.dadS()
objM = mother()
objM.moms()
objS = child()
objS.sonS()
