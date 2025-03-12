n = int(input())
score = list(map(int,input().split())) # 리스트 한줄에 입력받기

m = max(score)

for i in range(n):
    score[i]=score[i]/m*100

print(sum(score)/n)