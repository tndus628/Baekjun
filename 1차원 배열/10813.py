n,m = map(int, input().split())
list = []
for a in range(n):
    list.append(a+1)

for a in range(m):
    i,j = map(int, input().split())
    list[i-1],list[j-1] = list[j-1], list[i-1]

for a in range(n):
    print(list[a], end=' ')