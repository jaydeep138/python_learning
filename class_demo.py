class Person:
    def __init__(self,first_name,last_name,age):
        self.f=first_name
        self.l=last_name
        self.a=age
        self.c=first_name +"  "+ last_name

p1=Person('jaydeep','mulani',19)
print(p1.c)
