n, m= map(int,input().split())

a=[]
b=[]
# c=[]
for i in range(n):
    a += [[int(x) for x in input().split()]]

for i in range(n):
    b += [[int(y) for y in input().split()]]

for i in range(n):
    for j in range(m):
        print(a[i][j]+b[i][j],end=" ")
    print()
