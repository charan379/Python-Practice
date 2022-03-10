class Mobile:
    def __call__(self, *args, **kwargs):
        print("From Call")
        for x in args:
            print(x)

        for x, y in kwargs.items():
            print(x, y)

    def __init__(self, *args, **kwargs):
        print("From INIT")
        for x in args:
            print(x)

        for x, y in kwargs.items():
            print(x, y)
    global pall
    def pall(self, *args, **kwargs):
        print('from pall')
        for x in args:
            print(x)

        for x, y in kwargs.items():
            print(x, y)

a = Mobile(1,2, model = "x20")

a(1,2, model = "x20")



pall(1,2, model = "x20")