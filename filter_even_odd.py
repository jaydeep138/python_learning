def filter(l):
    even=[]
    odd=[]
    for i in l:
        if int(i) % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return [odd,even]

n=int(input("enter the length of the list:"))
numbers=[]
print("enter only even or odd number:")
for i in range(n):
    m=int(input())
    numbers.append(m)

print(filter(numbers))
