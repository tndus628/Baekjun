import sys 
input = sys.stdin.readline

n,m=map(int,input().split())
data = [[0]*(n+1)]
dsum=[[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    data += [[0]+[int(x) for x in input().split()]]


for i in range(1,n+1):
    for j in range(1,n+1):
        dsum[i][j] = dsum[i][j-1]+dsum[i-1][j]-dsum[i-1][j-1]+data[i][j]
        
for i in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    total = dsum[x2][y2]-dsum[x1-1][y2]-dsum[x2][y1-1]+dsum[x1-1][y1-1]
    print(total)
