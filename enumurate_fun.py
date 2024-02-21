#how we track the position of list items without enumerate function

#pos=0
#for name in names:
#    print(f"{pos} -----> {name}")
#    pos+=1

#with enumerate function
#for pos,name in enumerate(names):
#    print(f"{pos}--->{name}")

def fun(l,m):
    for pos,name in enumerate(l):
        if name==m:
            return f"{pos}-->{name}"
    if m not in l:
        return -1    


names=['jd','mulani','abc','xyz']
name=input("enter the target name : ")
print(fun(names,name))