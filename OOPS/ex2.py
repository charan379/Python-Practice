class Mobile:
    def __init__(self):
        self.model = "Model"
        self.ram = "ram"
        self.rom = 'rom'
        print("Class Initialized")
    def info(self):
        print(f'showing mobile info of : {self.model}')
        print(f'Model : {self.model}')
        print(f'Ram   : {self.ram}')
        print(f'Rom   : {self.rom}')

obj1 = Mobile()
obj1.model = "X20"
obj1.ram = "16GB"
obj1.rom = "128GB"

obj1.info()
