def square_numbers(l):
    m=[]
    for i in l:
        m.append(i*i)
    return m

numbers = []
n = int(input("enter the size of list : "))
for i in range(n):
    x=int(input(f"enter the {i} value :"))
    numbers.append(x)

print(square_numbers(numbers))
