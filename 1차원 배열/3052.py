A = []
remainder = []
outcnt=0
for i in range(10):
    A.append(int(input()))
    remainder.append(A[i]%42)

print(len(set(remainder))) #중복을 허용X
