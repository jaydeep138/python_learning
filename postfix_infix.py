class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def display(self):
        return self.stack
   

a=Stack()
exp=input("enter the postfix expression :")
for i in exp:
    if (i>='a' and i<='z') or (type(i) is int) or (i>='A' and i<='Z'):
        a.push(i)
    if i=='+' or i=='-' or i=='*' or i=='/':
        x=a.pop()
        y=a.pop()
        a.push(y+i+x)

print(a.display())

         