def list_count(l):
    count=0
    for i in l:
        if type(i)==list:
            count+=1
    return count


name=[1,2,[1,2,3],[3,4],3]
print(list_count(name))