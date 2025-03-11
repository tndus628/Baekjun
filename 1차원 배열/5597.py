list = []
std = []
k=0
for i in range(28):
    n = int(input())
    std.append(n)

std.sort()
for i in range(30):
    for j in std:
        if (i+1) ==j:
            k=0
            break
        else:
            k=1
    if k==1:
        list.append(i+1)
        k=0

print(*list) #배열 앞에 * 붙이면 요소만 출력