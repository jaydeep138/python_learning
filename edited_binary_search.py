def binary_search(l1,n,target):
    if target<=l1[0]:
        return l1[0]
    if target>=l1[n-1]:
        return l1[n-1]
    i=0;j=n
    while i<j:
        mid = (i+j)//2
        if l1[mid]==target:
            return l1[mid]
        if target<l1[mid]:
            if mid>0 and target>l1[mid-1]:
                return getcl(l1[mid-1],l1[mid],target)
            j=mid
        else:
            if mid<n-1 and target<l1[mid+1]:
                return getcl(l1[mid],l1[mid+1],target)
            i=mid+1
    return l1[mid]
def getcl(v1,v2,target):
    if target-v1>=v2-target:
        return v2
    else:
        return v1
o,m=map(int,input().split())
matrix=[(sorted(list(map(int,input().split())))) for i in range(o)]
#print(matrix)
main_min=10**9+9
for i in range(o-1):
    min_value=10**9+9
    y=matrix[i+1]
    #print(y)
    for j in matrix[i]:
        diff=binary_search(y,m,j)
        if abs(diff-j)<min_value:
            min_value=abs(diff-j)
    #print(min_value)
    if min_value<main_min:
        main_min=min_value
print(main_min)