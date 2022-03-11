"""
Polymorphism means ability of a thing to take
many forms

"""


class Duck:
    @staticmethod
    def sound():
        print('Quack Quack')


class Dog:
    @staticmethod
    def sound():
        print('Bhow... Bhow...')


def anysound(obj):
    obj.sound()


x = Duck()
anysound(x)

y = Dog()
anysound(y)
