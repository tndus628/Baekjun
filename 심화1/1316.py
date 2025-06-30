n = int(input())
cnt=n
for i in range(n):
    k=0
    m = input()
    for j in range(len(m)-1):
        if m[j]==m[j+1]:
            pass
        else:
            if m.find(m[j],j+1,len(m))>0:
                k=-1
    if k==-1:
        cnt-=1
print(cnt)