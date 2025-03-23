n = input().upper()
cntlist=[]
m = list(set(n))
k=0
for i in m:
    cntlist.append(n.count(i))

if cntlist.count(max(cntlist))>1:
    print("?")
else:
    print(m[cntlist.index(max(cntlist))])