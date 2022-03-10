# Class is blueprint or a design
class Moble:
    x = 99
    y = 1

    def add(self):
        return self.x + self.y

oobj = Moble()
oobj.x = 2
oobj.y = 3

# tr = Moble.add(oobj)
# or
tr = oobj.add()
print(tr)