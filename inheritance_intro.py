class Phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def specification(self):
        return f"{self.brand} {self.model} price is {self.price}"

class Smartphone(Phone):
    def __init__(self,brand,model,price,ram,memory,camera):
        #Phone.__init__(self,brand,model,price)
        super().__init__(brand,model,price)
        self.ram=ram
        self.memory=memory
        self.camera = camera

    def specification(self):
        return f"this phone has {self.ram} ram and {self.memory} internal storage and {self.camera} rear camera"
    

p1=Phone('nokia','1100',1000)
p2=Smartphone('oneplus','6 pro',35000,'6 gb','64 gb','32 mp')
#print(p1.specification())
#print(p2.specification())
print(p1.price,p1.model,p1.brand)