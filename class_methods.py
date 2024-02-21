class Phone:
    def __init__(self,brand,model,price):
        self.b=brand
        self.m=model
        self._p=max(price,0)

    @property
    def full_info(self):
        return f"brand is {self.b} model is {self.m} and price is {self._p}"

    @property
    def price(self):
        return self._p
    @price.setter
    def price(self,new_price):
        self._p=max(new_price,0)

p1=Phone('samsam','11j',200)
p1.price=-4000
print(p1.price)
print(p1.full_info)