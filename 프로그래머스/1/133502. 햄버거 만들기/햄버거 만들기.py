def solution(ingredient):
    temp = []
    answer = 0
    for i in ingredient:
        temp.append(i)
        if temp[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                temp.pop()
    return answer