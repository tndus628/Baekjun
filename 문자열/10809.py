s = input()
for i in range(97,123):
    idx=-1
    for j in range(len(s)):
        if chr(i)==s[j]: #아스키 숫자 문자로 변경
            idx = j
            break
        
    print(idx, end=' ')

# s = input()
# for i in range(97,123):
#     if chr(i) in s:
#         print(s.index(chr(i)),end=' ') #문자열 s에서 chr(i)가 처음 등장하는 위치 반환
#     else:
#         print("-1", end=' ')