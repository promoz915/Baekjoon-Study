import sys; input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
answer = 0

def merge_sort(start, end):                 # 리스트 시작과 끝
    global answer, arr
    if start < end:
        mid = (start + end) // 2            # index 반으로 자르기
        merge_sort(start, mid)              # 반으로 잘린 앞부분 재귀함수로 병합
        merge_sort(mid + 1, end)            # 반으로 잘린 뒷부분 재귀함수로 병합
        temp = []
        x, y = start, mid + 1               # x : 앞 쪽 그룹 시작점, y : 뒤 쪽 그룹 시작점

        while x <= mid and y <= end:
            if arr[x] <= arr[y]:
                temp.append(arr[x])
                x += 1
            else:
                temp.append(arr[y])
                y += 1
                answer += (mid - x) + 1     # 뒤 쪽 그룹 데이터가 더 작다면 answer 업데이트

        if x <= mid:                        
            temp = temp + arr[x:mid + 1]    
        if y <= end:
            temp = temp + arr[y:end + 1]
        for i in range(len(temp)):
            arr[start + i] = temp[i]

merge_sort(0, n-1)
print(answer)