def maximum(x,y,z):
    if x>y and x>z:
        return f"{x} is bigger"
    elif x>y and x<z:
        return f"{z} is bigger"
    else:
        return f"{y} is bigger"

num1 = int(input("enter 1st number : "))
num2 = int(input("enter 2nd number : "))
num3 = int(input("enter 3rd number : "))
print(maximum(num1,num2,num3))