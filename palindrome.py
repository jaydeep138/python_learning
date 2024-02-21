a = [7,4,20,15,3,6,9,8]
global ctr
def dvc(l, r,x):
    global ctr
    if l > r:
        return -1
    ctr += 1
    mid = (l + r)// 2
    if a[mid] == x:
        return mid
    else:
        temp = dvc(l, mid - 1, x)
        if temp == -1:
            temp = dvc(mid + 1, r, x)
        return temp
    
ctr = 0
print(dvc(0, len(a) - 1, 7))
print(ctr)

