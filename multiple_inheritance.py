class A:
    def methoda(self):
        return "just fun a"
    def hello(self):
        return "hey you a"

class B:
    def methodb(self):
        return "just fun b"
    def hello(self):
        return "hey you b"
    
class C(B,A):
    pass

c=C()
print(c.hello())
print(C.mro())
print(C.__mro__)
