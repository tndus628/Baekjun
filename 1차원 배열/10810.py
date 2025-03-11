n, m = map(int,input().split())
list = [0] * n #리스트에 N개의 0으로 채워진 리스트 만들어져서 특정 인덱스에 값을 바로 할당 가능
for a in range(m):
    i,j,k = map(int,input().split())
    for b in range(i,j+1):
        list[b-1] = k

for a in range(n):
    print(list[a], end=" ")