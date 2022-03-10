class Mobile:
    def __init__(self, model, ram, rom):
        self.model = model
        self.ram = ram
        self.rom = rom
    def info(self):
        print(f'Model : {self.model}')
        print(f'ram   : {self.ram}')
        print(f'Model : {self.rom}')


obj1 = Mobile("x20", "12GB", "128GB")
obj1.model = "X20"
obj1.info()

