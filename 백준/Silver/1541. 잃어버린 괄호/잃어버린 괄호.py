import sys; input = sys.stdin.readline

a = list(map(str, input().split("-")))      # - 부호에 따라 리스트 나눠서 입력
ans = 0

def mySum(i):                               # 현재 string에 있는 수를 모두 더하는 함수 구현
    sum = 0
    temp = str(i).split("+")                # + 부호에 따라 split
    for i in temp:                          # 나뉜 데이터 개수만큼 반복
        sum += int(i)                       # 입력받은 str값을 int값으로 변환해 저장
    return sum                              # 전체 값 리턴

for i in range(len(a)):
    temp = mySum(a[i])                      # 결괏값
    if i == 0:                              # 가장 앞 데이터일 때
        ans += temp                         # 가장 앞에 있는 값만 결괏값 더하기
    else:                                   # 아니라면
        ans -= temp                         # 뒷부분의 값은 합쳐서 결괏값 빼기

print(ans)