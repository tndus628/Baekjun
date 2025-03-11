while True:
    try:
        a, b= map(int,input().split()) #한번에 여러 정수 입력받기기
        print(a+b)
    except:
        break
# try-except 구문: try 구문에서 에러 발생 시 except 블록 코드 실행