# a,b = map(int,input().split())
# a_rev=0
# b_rev=0

# while a>0:
#     a_rev*=10
#     a_rev+=a%10
#     a//=10

# while b>0:
#     b_rev*=10
#     b_rev+=b%10
#     b//=10
# print(max(a_rev,b_rev))

a,b,=input().split()
a = int(a[::-1])
b = int(b[::-1])
print(max(a,b))