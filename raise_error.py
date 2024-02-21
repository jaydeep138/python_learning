#def add(a,b):
#    if (type(a) is int) and (type(b) is int):
#        return a+b
#    raise TypeError("oops you entered wrong type of input")

#print(add('s',3))

class Phone:
    def __init__(self,name):
        self.name=name

class Mobile_store:
    def __init__(self):
        self.mobiles=[]
    def add_mobile(self,new_mobile):
        if isinstance(new_mobile,Phone):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError("new mobile should be object of mobile class")

oneplus=Phone("one plus 6")
samsung=("samsung galaxy note 8")
Mobostore=Mobile_store()
Mobostore.add_mobile(oneplus)
jd=Mobostore.mobiles
print(jd[0].name)