n, m = map(int, input().split())
list = [i+1 for i in range(n)]

for a in range(m):
    i, j = map(int, input().split())
    list[i-1:j] = list[i-1:j][::-1] #리스트 일부 가져오고, 가져온 것을 뒤집음
print(*list)