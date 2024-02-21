class Circle:
    pie=3.14
    def __init__(self,radius):
        self.r=radius

    cr = lambda self : 2*Circle.pie*self.r

c=(Circle(4))
print(c.cr())