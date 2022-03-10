# base class

class names:
    dad = ''
    mom = ""
    son = ""


# Derived 1
class father(names):
    def dadS(self):
        print(self.dad)


# Derived 2
class mother(names):

    def moms(self):
        print(self.mom)


# Derived 3
class child(names):

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
