n, m= map(int,input().split())

a=[]
b=[]
# c=[]
for i in range(n):
    a += [list(input().split())]

for i in range(n):
    b += [list(input().split())]

print(type(a))
# print(b)
# for i in range(n):
#     for j in range(m):
#         print(a[i][j])
#         print(b[i][j])
#         c = a[i][j] + b[i][j]
#         print(c)
# for i in range(n):
#     for j in range(m):
#         print(c[i][j])