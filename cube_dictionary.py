def cube(a):
    user={}
    for i in range(1,a+1):
        user[f"number {i}"]= i*i*i
    return user

num=int(input("enter the number : "))
print(cube(num))
