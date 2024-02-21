class Que:
    max=5
    front=-1
    rear=-1
    def __init__(self):
        self.q=[]
    def insert(self,item):
        if Que.front==-1:
            Que.front=0
            Que.rear=0
            self.q.append(item)
        else:
            if Que.rear==Que.max-1:
                print("queue is overflow")
            else:
                self.q.append(item)
                Que.rear+=1
    def delete(self):
        if Que.front==-1 or Que.front>Que.rear:
            print("queue is underflow")
        else:
            print(Que.front)
            x=self.q.pop(0)
            if Que.front==Que.max-1:
                Que.front=-1
                Que.rear=-1
            else:
                Que.front+=1
            return x

    def display(self):
        return self.q

a=Que()
print("welcome to the queue operations")
print("1.insert 2.delete 3.display 4.exit")
while True:
    n=int(input("enter your choide : "))
    if n==1:
        a.insert(int(input("enter the number you want to insert : ")))
    if n==2:
        print(f"deleted item is {a.delete()}")
    if n==3:
        print(a.display())
    if n==4:
        break

