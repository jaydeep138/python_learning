n,m,q=map(int,input().split())
a=[[0 for i in range(m)] for j in range(n)]
for i in  range(q):
    x,y=map(int,input().split())
    for j in range(m):
       a[x-1][j]+=1
    for j in range(n):
       a[j][y-1]+=1
print(a)