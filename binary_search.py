def bin_search(L,N,item):
    l=0
    u=N-1
    while l<=u:
        m=int((l+u)/2)
        if item==L[m]:
            print(f'your item is found at index {m}')
            return
        elif item>L[m]:
            l=m+1
        else:
            u=m-1
    print("unsuccessfull search no found ")

n=int(input("enter the size of list : "))
L=[int(i) for i in input().split()]
item=int(input("enter the numberyou want to find : "))
bin_search(L,n,item)