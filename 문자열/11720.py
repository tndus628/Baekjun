n = int(input())
arr = list(map(int,input())) #공백없이 여러개 입력받기
sum=0

for i in range(n):
    sum+=arr[i]
print(sum)