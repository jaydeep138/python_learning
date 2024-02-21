def maximum(a,i,c):
    if i>=c-2:
        if a[i]>a[i+1]:
            return a[i]
        else:
            return a[i+1]
    
    m=maximum(a,i+1,c)

    if m>a[i]:
        return m
    else:
        return a[i]


x=[]
n=int(input("enter the size of the array : "))
print("enter the value of array elements :")
for i in range(n):
    x.append(int(input()))

print(maximum(x,0,n))
