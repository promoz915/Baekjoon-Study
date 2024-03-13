# A와 B를 입력받기
A, B = map(int, input().split())

# A와 B의 범위 확인
if 0 < A < 10 and 0 < B < 10:
    # A와 B의 합을 계산
    result = A + B
    # 결과 출력
    print(result)
else:
    print("error")
