# Parent Class
class parent:
    x = 10

    def SayHello(self):
        print("Hello from parant")

# child class
class child(parent):
    y = 20

    def SayBye(self):
        print("Bye Bye from child")


obj = child()
obj.SayHello()
print(obj.x , obj.y)

obj.SayBye()