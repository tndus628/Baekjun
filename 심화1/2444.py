# n = int(input())

# for i in range(n):
#     for j in range(n-1,i,-1):
#         print(" ",end='')
#     for j  in range(i*2+1):
#         print("*", end='')
#     print()
    
# for i in range(1,n):
#     for j in range(i):
#         print(" ",end='')
#     for j in range((n-i)*2-1,0,-1):
#         print("*",end='')
#     print()

n = int(input())
for i in range(n):
    print(" " * (n-1-i) + "*" * (i*2+1))
for i in range(1,n):
    print(" " * i + "*" * ((n-i)*2-1))