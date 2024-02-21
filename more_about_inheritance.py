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
    
class Iphone(Smartphone):
    def __init__(self,brand,model,price,ram,memory,camera,security):
        super().__init__(brand,model,price,ram,memory,camera)
        self.security=security

    def specification(self):
        return f"this iphone has {self.ram} ram and {self.memory} internal storage and {self.camera} rear camera and it has {self.security} sensor"

p1=Phone('nokia','1100',1000)
p2=Smartphone('oneplus','6 pro',35000,'6 gb','64 gb','32 mp')
p3=Iphone('apple','iphone x',75000,'3 gb','128 gb','12 mp','fingerprint')
#print(p1.specification())
#print(p2.specification())
#print(p3.specification())
#print(isinstance(p3,Phone))
#print(isinstance(p2,Smartphone))
#print(isinstance(p1,Smartphone))
#print(issubclass(Smartphone,Phone))
#print(issubclass(Iphone,Smartphone))
#print(issubclass(Phone,Smartphone))
print(issubclass(Phone,Iphone))