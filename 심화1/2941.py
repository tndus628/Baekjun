n = input()
croatia=['c=','c-','dz=','d-','lj','nj','s=','z=']

# for i in croatia:
#     m = n.find(i)
#     if m>=0:
#        n=n.replace(n[m:m+len(i)],"*")
# print(len(n))

for i in croatia:
    n = n.replace(i,"*")
print(len(n))